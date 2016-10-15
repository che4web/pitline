from django.db import models

# Create your models here.
class Action(models.Model):
    title = models.CharField(max_length=255)

    text = models.TextField()
    img = models.ImageField()
    date= models.DateField(auto_now_add=True)

