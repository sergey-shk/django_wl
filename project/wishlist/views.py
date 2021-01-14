from django.shortcuts import render, HttpResponse, redirect
from .services import wishlist, users
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'index.html')


def register(request):
    if request.method != 'POST':
        return redirect('index')
    users.register(request)
    return redirect('index')


def login(request):
    if request.method != 'POST':
        return redirect('index')
    users.login(request)
    return redirect('index')


def logout(request):
    if request.method != 'POST':
        return redirect('index')
    auth.logout(request)
    return redirect('index')


def about(request):
    return HttpResponse('About page')


def example(request):
    response = wishlist.ex()
    return response
