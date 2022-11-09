from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('portfolio', views.portfolio, name="portfolio"),
    path('trade', views.trade, name="trade"),
    path('research', views.research, name="research"),
    path('learn', views.learn, name="learn"),
    path('game', views.game, name="game"),
    path('home', views.home, name="home"),
]
