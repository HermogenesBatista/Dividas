# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

__author__ = 'Moginho'

from django.conf.urls import patterns, url
from Cartoes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<cartao_id>\w+)/resultado/$', views.resultado, name='resultado'),
)
