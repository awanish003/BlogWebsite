from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.handelsignUp, name='handlesignUp'),
    path('login', views.handelLogin, name='handleLogin'),
    path('logout', views.handelLogout, name='handleLogout'),
]