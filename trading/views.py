from django.shortcuts import render
# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
    return render(request, "home.html")


@login_required(login_url='/login')
def portfolio(request):
    return render(request, "portfolio.html")


@login_required(login_url='/login')
def game(request):
    return render(request, "games.html")


@login_required(login_url='/login')
def learn(request):
    return render(request, "learn.html")


@login_required(login_url='/login')
def research(request):
    return render(request, "research.html")


@login_required(login_url='/login')
def trade(request):
    return render(request, "trade.html")
