from django.db import models

# Create your models here.

class Buzzword(models.Model):
    word = models.CharField(max_length=50)

    def __unicode__(self):
        return self.word

class WinCondition(models.Model):
    name = models.CharField(max_length=50)
    code = models.TextField()

    def __unicode__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=50)
    words = models.ManyToManyField(Buzzword)
    win_conditions = models.ManyToManyField(WinCondition)

    def __unicode__(self):
        return self.name
    
