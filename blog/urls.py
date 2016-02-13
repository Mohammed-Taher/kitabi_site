from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.show_post, name="show_post"),
]
