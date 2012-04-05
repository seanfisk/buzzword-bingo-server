from django.db import models

# Create your models here.

class Buzzword(models.Model):
    word = models.CharField(max_length=50)
