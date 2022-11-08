from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.home,name="signup"),
    path('index',views.signin,name="index"),
    path('signout',views.signout,name="signout"),
    
]
