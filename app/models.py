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

