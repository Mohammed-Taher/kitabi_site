from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.view_book, name='view_book'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.view_author, name='view_author'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
]
