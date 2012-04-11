from django.core.urlresolvers import reverse
from djangorestframework.views import View

class BuzzwordBingoView(View):
    def get(self, request):
        return [{'name': 'Buzzwords', 'url': reverse('buzzword-root')},
                {'name': 'Win Conditions', 'url': reverse('win-condition-root')},
                {'name': 'Boards', 'url': reverse('board-root')},
                ]
