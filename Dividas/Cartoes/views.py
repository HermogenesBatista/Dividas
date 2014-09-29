# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from Cartoes.models import *

# Create your views here.
def index(request):
    lastest_cartoes = Cartao.objects.order_by('-nome')[:5]
    template = loader.get_template('Cartoes/index.html')
    context = RequestContext(request, {
        'latest_cartoes': lastest_cartoes,
    })
    return HttpResponse(template.render(context))


def resultado(request, cartao_id):

    if(cartao_id.isalpha()):
        if(cartao_id == 'all'):
            c = Cartao.objects.all()
        else:
            return HttpResponse('Erro na sua busca!.')

    else:
        c = [Cartao.objects.get(pk=cartao_id)]

    template = loader.get_template('Cartoes/resultado.html')
    context = RequestContext(request, {
        'cartoes': c,
    })
    return HttpResponse(template.render(context))

