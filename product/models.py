import uuid
from django.db import models


class Bottles(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, default="" )
    volume = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    # material = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    # image = models.ImageField(upload_to='bottles', default='default.png')
    price = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    neck_diameter = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name="flakons" )
    field = models.ForeignKey('FieldCategory', on_delete=models.SET_NULL, null=True, blank=True, related_name="flakons")
    min_order = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Images(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image = models.ImageField(upload_to='bottles', default='default.png')
    created = models.DateTimeField(auto_now_add=True)
    bottle = models.ForeignKey(Bottles, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return self.image.name


class FieldCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Settings(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    total = models.IntegerField(default=1)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    bottle = models.ForeignKey(Bottles, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.phone

