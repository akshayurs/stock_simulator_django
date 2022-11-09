from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login_, name="login"),
    path('logout', views.logout_, name="logout"),
]
