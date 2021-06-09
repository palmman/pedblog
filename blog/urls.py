from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('register', views.register , name='register'),
    path('login', views.login , name='login'),
    path('logout', views.logout, name='logout'),
    path('<slug:post_slug>', views.single_post , name='single_post'),
]
