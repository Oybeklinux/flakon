from django.contrib import admin
from .models import *


class BottleAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "created"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["bottle", "total", "created", "phone"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created"]


class SettingsAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created"]


admin.site.register(Bottles, BottleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
