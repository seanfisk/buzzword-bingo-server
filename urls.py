from django.conf.urls.defaults import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from buzzwordbingo.resources import (BuzzwordResource, WinConditionResource,
                                     BoardResource)
from buzzwordbingo.views import BuzzwordBingoView

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^$', BuzzwordBingoView.as_view()),
    url(r'^buzzwords/$', 
        ListOrCreateModelView.as_view(resource=BuzzwordResource),
        name='buzzwords-root'),
    url(r'^buzzwords/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BuzzwordResource),
        name='buzzwords-instance'),
    url(r'^win-conditions/$',
        ListOrCreateModelView.as_view(resource=WinConditionResource),
        name='win-conditions-root'),
    url(r'^win-conditions/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=WinConditionResource),
        name='win-conditions-instance'),
    url(r'^boards/$',
        ListOrCreateModelView.as_view(resource=BoardResource),
        name='boards-root'),
    url(r'^boards/(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BoardResource),
        name='boards-instance'),

    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)    
