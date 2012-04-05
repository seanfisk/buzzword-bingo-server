from django.conf.urls.defaults import patterns, url
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from bingo.models import Buzzword

class BuzzwordResource(ModelResource):
    model = Buzzword

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^$', ListOrCreateModelView.as_view(resource=BuzzwordResource)),
    url(r'^(?P<pk>[^/]+)/$',
        InstanceModelView.as_view(resource=BuzzwordResource)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
