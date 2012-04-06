from bingo.models import Buzzword, WinCondition, Board
from djangorestframework.resources import ModelResource

class BuzzwordResource(ModelResource):
    model = Buzzword
    # fields = ('word')

class WinConditionResource(ModelResource):
    model = WinCondition
    # fields = ('code')

class BoardResource(ModelResource):
    model = Board
    # fields = ('words', 'win_conditions')
