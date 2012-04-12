from django.core.urlresolvers import reverse
from djangorestframework.views import View

class BuzzwordBingoView(View):
    """The buzzword bingo REST API provides an interface to a collection of
    boards, which contain the buzzwords on the board and a list of win
    conditions, which are Python code which determines if a given board is a
    winning board.

    For more about the game of buzzword bingo, please see the [Buzzword Bingo
    article on Wikipedia](http://en.wikipedia.org/wiki/Buzzword_bingo).
    """
    def get(self, request):
        return [{'name': 'Buzzwords', 'url': reverse('buzzword-root')},
                {'name': 'Win Conditions', 'url': reverse('win-condition-root')},
                {'name': 'Boards', 'url': reverse('board-root')},
                ]
