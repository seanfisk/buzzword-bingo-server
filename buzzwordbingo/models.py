""":mod:`buzzwordbingo.models` --- Application models
"""

from django.db import models
from djangotoolbox.fields import ListField

class Buzzword(models.Model):
    """
    A single buzzword.
    
    .. todo:: Ensure that the deletion of a buzzword in a board is prevented, or that it
      cascades. Preferably the former over the latter.
    """
    word = models.CharField(max_length=50)

    def __unicode__(self):
        return self.word

class WinCondition(models.Model):
    """
    Python code which determines whether a given board is a winning board.
    
    .. todo:: Validate the Python code that comes as text.
    .. todo:: Decide on a standard format for this code.
    """
    name = models.CharField(max_length=50, unique=True)
    code = models.TextField(
        help_text='Code which determines whether the board is a winning board.')

    def __unicode__(self):
        return self.name

class Board(models.Model):
    """
    A list of words composing a full bingo board and a list of win conditions.
    
    .. todo:: Do some validation to ensure that boards must be square.
    """
    name = models.CharField(max_length=50)
    # words = models.ManyToManyField(Buzzword)
    # win_conditions = models.ManyToManyField(WinCondition)
    words = ListField(help_text='List of word ids.')
    win_conditions = ListField(help_text='List of win_condition ids.')

    def __unicode__(self):
        return self.name
    
