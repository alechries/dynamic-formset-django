from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)


class Addition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)