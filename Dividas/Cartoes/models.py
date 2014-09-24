# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from datetime import *


# Create your models here.

class Bandeira(models.Model):
    nome = models.CharField(max_length=50, verbose_name=u"Texto Aqui")

    situacao = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.nome

class Cartao(models.Model):
    nome = models.CharField(max_length=50, verbose_name=u"Texto Aqui")
    validade = models.CharField(max_length=7)
    vencimento = models.IntegerField(default=1)
    limite = models.FloatField(default=510)
    bandeira = models.ForeignKey(Bandeira, default=1)
    situacao = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % self.nome

    def bestDayBuy(self):
        self._bestday = self.vencimento - 10

        if(self._bestday<0):
            self._bestday += 30

        hoje = date.today()
        self._dtBestDay = date(hoje.year, hoje.month, self._bestday)
        return self._bestday


    def parcialFatura(self):
        compras = self.compra_set.all()

        soma = 0

        for compra in compras:
            intervalo = self.proxFatura() - compra.datacompra
            if(intervalo.days > 40):
                soma += compra.valor

        return soma

    def proxFatura(self):
        hoje = date.today()
        mes = hoje.month
        ano = hoje.year
        if(hoje.day > self.vencimento):
            mes += 1

            if(mes > 12):
                mes -= 12
                ano += 1

        return date(ano, mes, self.vencimento)
    '''
    linha abaixo serve para dar uma descrição quando usar os metodos criados
    automaticamente são renomeados no Django-admin
    '''
    bestDayBuy.short_description = 'Melhor dia de Compra'
    proxFatura.short_description = 'Data da Prox. Fatura'
    parcialFatura.short_description = 'Parcial da Prox. Fatura'


class Compra(models.Model):
    cartao = models.ForeignKey(Cartao)
    descricao = models.CharField(max_length=50, verbose_name=u"Texto Aqui")
    valor = models.FloatField(default=5)
    qtparcelas = models.IntegerField(default=1)
    datacompra = models.DateField('Data da Compra')
    situacao = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s dtcompra: %s' % (self.descricao, str(self.datacompra))

    def parcelasPg(self):
        hoje = date.today()
        parcpg = hoje.month - self.datacompra.month

        return parcpg

    def parcelasRest(self):
        return self.qtparcelas - self.parcelasPg()

