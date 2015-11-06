# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from Cartoes.models import *
from .forms import FormCartao

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
            raise Http404

    else:
        c = [get_object_or_404(Cartao, pk=cartao_id)]

    template = loader.get_template('Cartoes/resultado.html')
    context = RequestContext(request, {
        'cartoes': c,
    })
    return HttpResponse(template.render(context))

def cartao_add(request):
    extra = {}
    if request.method == "POST":
        form = FormCartao(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Salvo Com Sucesso!'
        else:
            msg = 'Error ao Tentar Salvar!'
        extra = {'msg': msg}
    else:
        form = FormCartao()
    data = {
        'form': form,
        'title': "Add Cartões",
        'extra': extra
    }

    return render(request, 'Cartoes/form_cartao.html', data)