#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<user_id>[-\d]+)$', views.index),
]
