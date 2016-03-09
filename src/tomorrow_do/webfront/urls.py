# coding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^main$', views.MainView.as_view(), name="main"),
    url(r'^$', views.RootView.as_view(), name="root"),
]
