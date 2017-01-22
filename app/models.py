#! -*- coding=utf-8 -*-
"""
Definition of models.
"""

from django.db import models

# Create your models here.
DEFAULT_PHOTO = "/static/default_photo.png"
class Feedback(models.Model):
    name = models.CharField(max_length=255,blank=True,verbose_name=u'название')
    title = models.CharField(max_length=255,blank=True,verbose_name=u'заголовок')
    text = models.TextField(blank=True,verbose_name=u'текст')
    foto = models.ImageField(verbose_name=u'фото')
    active = models.BooleanField(blank=True,verbose_name=u'На главной?')
    date = models.DateField(auto_now_add = True,verbose_name=u'дата создания')

    def get_foto(self):
        if self.foto:
            return self.foto.url
        else:
            return DEFAULT_PHOTO
    class Meta:
        verbose_name=u'Отзыв'
        verbose_name_plural=u'Отзывы'
    def __str__(self):
        return str(self.id)+'-- '+self.name
class Project(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'Имя')
    title = models.CharField(max_length=255,verbose_name=u'Заголовок')
    text = models.TextField(verbose_name=u'текст')
    foto_befo = models.ImageField(blank=True,verbose_name=u'до')
    foto_after = models.ImageField(blank=True,verbose_name=u'после')
    active = models.BooleanField(blank=True,verbose_name=u'до')
    date = models.DateField(auto_now_add = True,verbose_name=u'до')
    time = models.CharField(max_length=255,verbose_name=u'время выполнения')
    cost = models.CharField(max_length=255,verbose_name=u'цена')

    def get_foto(self):
        if self.foto:
            return self.foto.url

    def __str__(self):
        return str(self.id)+'-- '+self.name
    class Meta:
        verbose_name=u'Проект'
        verbose_name_plural=u'Наши работы'
class Director(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'Имя')
    text_base = models.TextField(verbose_name=u'Основной текст')
    text_welcome = models.TextField(verbose_name=u'Текст приветствия')
    foto = models.ImageField(blank=True,verbose_name=u'фото')
    contact = models.TextField(verbose_name=u'контакты')

    def __str__(self):
        return str(self.id)+'-- '+self.name
    class Meta:
        verbose_name=u'Директор'
        verbose_name_plural=u'Директор'
