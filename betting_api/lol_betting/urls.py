from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lol_betting import views

urlpatterns = [
    url(r'^teams/$', views.TeamList.as_view()),
    url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view()),
    url(r'^matches/$', views.MatchList.as_view()),
    url(r'^matches/details/$', views.MatchDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)