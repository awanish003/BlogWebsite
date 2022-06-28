from re import M
from tkinter import N
from wsgiref.util import request_uri
from django.forms import modelformset_factory
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request):
    messages.success(request,'welcome to about')
    return render(request,'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        contents = request.POST['content']
        if len(name) < 1 or len(email) < 1 or len(phone) < 1 or len(contents) < 1 :
            messages.error(request, 'please fill in all ,Something is missing...')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=contents)
            contact.save()
            messages.success(request, 'Your form Has Been Submitted Successfully')
    return render(request,'home/contact.html')

def search(request):
    query = request.GET['search']
    # allposts = Post.objects.all()
    if len(query) > 80:
        allposts = Post.objects.none()
    else:
        allpoststitle = Post.objects.filter(title__icontains = query)
        allpostscontent = Post.objects.filter(content__icontains = query)
        allposts = allpoststitle.union(allpostscontent)
    if allposts.count() == 0:
        messages.warning(request, 'No search Results found , Try Searching With Relevent Words...')
    params = {'allposts': allposts, 'query':query}
    return render(request,'home/search.html',params)

def handelsignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #checks for errorneous inputs
        if len(username) > 10 :
            messages.error(request, "Unable To SignUp - Username Must not be more Than 10 Character")
            return redirect('home')

        if not username.isalnum() :
            messages.error(request, "Unable To SignUp - Username Must Only COntain Letters And Numbers")
            return redirect('home')

        if password1 != password2 :
            messages.error(request, "Unable To SignUp - Password do not Match")
            return redirect('home')

        #create the user
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your SignUp has Been Done Successfully!!!")
        return redirect('home')

    else:
        return HttpResponse("404- Not Found")

def handelLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername , password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username Or Password Try Again")
            return redirect('home')
    return HttpResponse("404- Not Found")
    
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')