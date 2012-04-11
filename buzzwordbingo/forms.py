from django import forms
from buzzwordbingo.models import Buzzword, Board, WinCondition

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = ('words', 'win_conditions')

    words = forms.TypedMultipleChoiceField(
        coerce=int,
        choices=[(word.pk, word.word) for word in Buzzword.objects.all()])
    """Re-define words to be a custom field on the form rather than a field
    straight from the model.
    """

    win_conditions = forms.TypedMultipleChoiceField(
        coerce=int,
        choices=[(win_condition.pk, win_condition.name)
                 for win_condition in WinCondition.objects.all()])
    """Re-define win_conditions to be a custom field on the form rather than
    straight from the model.
    """

