from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0, null=True, blank=True)


class TypeA(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AdditionA(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(default=0, null=True, blank=True)
    count_type = models.ForeignKey(TypeA, on_delete=models.CASCADE, null=True, blank=True)


class AdditionTypeA(models.Model):
    addition = models.ForeignKey(AdditionA, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeA, on_delete=models.CASCADE)


class AdditionB(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
