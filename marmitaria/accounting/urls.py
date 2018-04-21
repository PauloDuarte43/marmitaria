# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^receita', views.receita, name='receita'),
    url(r'^despesa', views.despesa, name='despesa'),
]
