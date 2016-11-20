"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()
    foto = models.ImageField(blank=True)
    active = models.BooleanField(blank=True)
    date = models.DateField(auto_now_add = True)

    def get_foto(self):
        if self.foto:
            return self.foto.url

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

