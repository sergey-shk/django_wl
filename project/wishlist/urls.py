from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create_wish_item', views.create_wish_item, name='create_wish_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('item/<int:item_id>/', views.item_details, name='item_details'),
    path('update/<int:item_id>', views.update_item, name='update_item')
]
