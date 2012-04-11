from django.db import models
from djangotoolbox.fields import ListField

# Create your models here.

class Buzzword(models.Model):
    word = models.CharField(max_length=50)

    def __unicode__(self):
        return self.word

class WinCondition(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.TextField(
        help_text='Code which determines whether the board is a winning board.')

    def __unicode__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=50)
    # words = models.ManyToManyField(Buzzword)
    # win_conditions = models.ManyToManyField(WinCondition)
    words = ListField(help_text='List of word ids.')
    win_conditions = ListField(help_text='List of win_condition ids.')

    def __unicode__(self):
        return self.name
    
