""":mod:`buzzwordbing.resources` --- Resources for the REST interface
"""

from buzzwordbingo.models import Buzzword, WinCondition, Board
from djangorestframework.resources import ModelResource
from buzzwordbingo.forms import BoardForm
from django.core.urlresolvers import reverse

# don't give these resources docstrings, because the docstrings are shown in the
# actual api, and the defaults make a lot of sense

class BuzzwordResource(ModelResource):
    model = Buzzword

class WinConditionResource(ModelResource):
    model = WinCondition

class BoardResource(ModelResource):
    form = BoardForm
    model = Board

    def words(self, instance):
        """Overridden method to return full URLs to each buzzword instance."""
        return [reverse('buzzword-instance',
                        args=[word_pk]) for word_pk in instance.words]

    def win_conditions(self, instance):
        """Overridden method to return full URLs to each win condition
        instance."""
        return [reverse('win-condition-instance',
                        args=[wc_pk]) for wc_pk in instance.win_conditions]
