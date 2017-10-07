# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=250,db_index=True)
    
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])

    def __unicode__(self):
        return self.name
class Product(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category,related_name='products')
    name = models.CharField(max_length=250,db_index=True)
    slug = models.SlugField(max_length=250,db_index=True,unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ('name',)
        index_together = (('id','slug'),)

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id, self.slug])
    def __unicode__(self):
        return self.name
class Slide(models.Model):
    objects = models.Manager()
    image = models.ImageField(upload_to='slide/%Y/%m/%d',blank=True)
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name