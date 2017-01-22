#! -*- coding=utf-8 -*-
"""
Definition of models.
"""

from django.db import models

# Create your models here.
DEFAULT_PHOTO = "/static/default_photo.png"
class Feedback(models.Model):
    name = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255,blank=True)
    text = models.TextField(blank=True)
    foto = models.ImageField()
    active = models.BooleanField(blank=True)
    date = models.DateField(auto_now_add = True)

    def get_foto(self):
        if self.foto:
            return self.foto.url
        else:
            return DEFAULT_PHOTO

class Project(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField(verbose_name=u'текст')
    foto_befo = models.ImageField(blank=True,verbose_name=u'до')
    foto_after = models.ImageField(blank=True,verbose_name=u'после')
    active = models.BooleanField(blank=True)
    date = models.DateField(auto_now_add = True)
    time = models.CharField(max_length=255,verbose_name=u'время выполнения')
    cost = models.CharField(max_length=255,verbose_name=u'цена')

    def get_foto(self):
        if self.foto:
            return self.foto.url

class Director(models.Model):
    name = models.CharField(max_length=255)
    text_base = models.TextField()
    text_welcome = models.TextField()
    foto = models.ImageField(blank=True)
    contact = models.TextField()
