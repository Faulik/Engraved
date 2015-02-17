from django.conf.urls import patterns, url
from raws_parser import views

urlpatterns = patterns('',
    url(r'^d3.json$', views.get_test_d3_json, name='json'),
    url(r'^packs$', views.Packs.as_view(), name='packs'),
    url(r'^packs/(?P<pack_name>[^/]+)/(?P<file_name>[^/]+)/$',
        views.Pack.as_view(), name='pack')
)