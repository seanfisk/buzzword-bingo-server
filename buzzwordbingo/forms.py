from django import forms
from buzzwordbingo.models import Buzzword

class BoardForm(forms.Form):
    words = forms.TypedMultipleChoiceField(
        coerce=int,
        choices=[(word.pk, word.word) for word in Buzzword.objects.all()])
