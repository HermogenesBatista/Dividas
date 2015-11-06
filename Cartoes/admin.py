# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from Cartoes.models import Cartao, Bandeira, Compra
from datetime import *


# Register your models here.
class CompraInline(admin.TabularInline):
    model = Compra
    extra = 3

class AdminCartao(admin.ModelAdmin):
    #fields=['nome','validade', 'vencimento','limite','bandeira']
    fieldsets = [
        (None,                      {'fields': ['situacao']}),
        (None,                      {'fields': ['nome', 'bandeira']}),
        ('Dados do Cartao ',        {'fields': ['validade', 'vencimento', 'limite']}),

    ]

    inlines = [CompraInline]
    list_display = ('nome', 'bandeira', 'validade', 'bestDayBuy', 'vencimento', 'proxFatura', 'parcialFatura')
    list_filter = ['bandeira', 'vencimento']

admin.site.register(Bandeira)
admin.site.register(Cartao, AdminCartao)

