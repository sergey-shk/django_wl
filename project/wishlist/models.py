from django.db import models
from django.contrib.auth.models import User


class WishItemCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class WishItem(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200, blank=True, null=True)
    store = models.CharField(max_length=100, blank=True, null=True)
    store_url = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(WishItemCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['date']

