from buzzwordbingo.models import Buzzword, WinCondition, Board
from djangorestframework.resources import ModelResource
from buzzwordbingo.forms import BoardForm

class BuzzwordResource(ModelResource):
    model = Buzzword
    # fields = ('word')

class WinConditionResource(ModelResource):
    model = WinCondition
    # fields = ('code')

class BoardResource(ModelResource):
    form = BoardForm
    model = Board
    # fields = ('words', 'win_conditions')

    # def words(self, instance):
    #     return 'blah'
