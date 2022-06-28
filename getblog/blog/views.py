from django.http import HttpRequest, HttpResponse ,HttpResponseRedirect
from django.shortcuts import redirect, render
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def bloghome(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/bloghome.html',context)
    # return HttpResponse("this is bloghome")

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] =[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'post': post, 'comments':comments,'replyDict':replyDict}
    return render(request, 'blog/blogpost.html',context)
    # return HttpResponse(f'this is blogpost  {slug}')

    
def postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get('comments')
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, "your comment has been posted succesfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request, "your reply has been posted succesfully")

    return redirect(f'/blog/{post.slug}')