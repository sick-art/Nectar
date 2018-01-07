# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .api import ListApi, CardApi

urlpatterns = {
    url(r'^lists/$', ListApi.as_view()),
    url(r'^cards/$', CardApi.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)