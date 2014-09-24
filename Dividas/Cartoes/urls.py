__author__ = 'Moginho'
from django.conf.urls import patterns, url

from Cartoes import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<cartao_id>\d+)/resultado/$', views.resultado, name='resultado'),
    url(r'(all)/resultado/$', views.resultado, name='resultado'),
)
