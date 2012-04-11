from django.core.urlresolvers import reverse
from djangorestframework.views import View

class BuzzwordBingoView(View):
    def get(self, request):
        return [{'name': 'Buzzwords', 'url': reverse('buzzwords-root')},
                {'name': 'Win Conditions', 'url': reverse('win-conditions-root')},
                {'name': 'Boards', 'url': reverse('boards-root')},
                ]
