# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url

from news.views import PostsListView, PostDetailView, listing

from . import views

urlpatterns = [
    url(r'^$', listing, name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
]