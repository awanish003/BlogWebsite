from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
# Api to post a comment
    path('postcomment', views.postcomment, name='PostComment'),
    
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]