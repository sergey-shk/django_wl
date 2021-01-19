from django.shortcuts import HttpResponse
from ..models import WishItem


def create_wish_item(request):
    new_item = WishItem.objects.create(name=request.POST['name'], owner=request.user, image_url=request.POST['image_url'])
    new_item.save()


def delete_item(item_id):
    WishItem.objects.get(id=item_id).delete()


def get_wish_list():
    wish_list = WishItem.objects.all()
    return wish_list


def get_item_details(item_id):
    return WishItem.objects.get(id=item_id)


def update_item(request, item_id):
    item = WishItem.objects.get(id=item_id)
    item.name = request.POST['name']
    item.image_url = request.POST['image_url']
    item.save()