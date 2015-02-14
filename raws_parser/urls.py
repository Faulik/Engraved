from django.conf.urls import patterns, url
from raws_parser.views import JsonResponse

urlpatterns = patterns('',
    url(r'^d3.json$', JsonResponse, name='json'),
)