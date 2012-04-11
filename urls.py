from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from buzzwordbingo.resources import (BuzzwordResource, WinConditionResource,
                                     BoardResource)
from buzzwordbingo.views import BuzzwordBingoView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^$', BuzzwordBingoView.as_view()),
    url(r'^buzzwords/$', 
        ListOrCreateModelView.as_view(resource=BuzzwordResource),
        name='buzzword-root'),
    url(r'^buzzwords/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BuzzwordResource),
        name='buzzword-instance'),
    url(r'^win-conditions/$',
        ListOrCreateModelView.as_view(resource=WinConditionResource),
        name='win-condition-root'),
    url(r'^win-conditions/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=WinConditionResource),
        name='win-condition-instance'),
    url(r'^boards/$',
        ListOrCreateModelView.as_view(resource=BoardResource),
        name='board-root'),
    url(r'^boards/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BoardResource),
        name='board-instance'),
    ('^_ah/warmup$', 'djangoappengine.views.warmup')
)
