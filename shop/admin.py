# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category,Product,Slide

# Register your models here.
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,ProductAdmin)
admin.site.register(Slide)

