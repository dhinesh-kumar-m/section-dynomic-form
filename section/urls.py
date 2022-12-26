from django.conf.urls import url

from section.views import SectionsListView,SectionsAddView,SectionUpdateView

app_name = "sections"

urlpatterns = [
    url(r'^$',SectionsListView.as_view(),name='index'),
    url(r"^(?P<pk>\d+)/$", SectionUpdateView.as_view(), name="update"),
    url(r'^create/$',SectionsAddView.as_view(),name='create')
]
