from django.conf.urls import url
from django.contrib import admin

from section.views import SectionsListView,SectionsAddView

app_name = "sections"

urlpatterns = [
    url(r'^$',SectionsListView.as_view(),name='index'),
    url(r'^create/$',SectionsAddView.as_view(),name='create')
]
