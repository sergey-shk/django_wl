from django.shortcuts import render, HttpResponse, redirect
from .services import wishlist, users
from django.contrib.auth.models import User
from django.contrib import auth


def index(request):
    if request.user.is_authenticated:
        data = {
            'wish_list': wishlist.get_wish_list()
        }
        return render(request, 'home.html', context=data)
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
    if not request.user.is_authenticated:
        return redirect('index')
    auth.logout(request)
    return redirect('index')


def create_wish_item(request):
    if request.method != 'POST':
        return redirect('index')
    wishlist.create_wish_item(request)
    return redirect('index')


def delete_item(request, item_id):
    if request.method != 'POST':
        return redirect('index')
    wishlist.delete_item(item_id)
    return redirect('index')


def item_details(request, item_id):
    item = wishlist.get_item_details(item_id)
    return render(request, 'item_detail.html', context={'item': item})


def update_item(request, item_id):
    wishlist.update_item(request, item_id)
    item = wishlist.get_item_details(item_id)
    return render(request, 'item_detail.html', context={'item': item})
