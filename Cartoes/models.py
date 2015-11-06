# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from datetime import *


# Create your models here.

class Bandeira(models.Model):
    nome = models.CharField(max_length=50, verbose_name=u"Nome da Bandeira")
    situacao = models.BooleanField(default=True, verbose_name=u"Situação")

    def __unicode__(self):
        return u'{nome:s}'.format(nome=self.nome)

class Cartao(models.Model):
    nome = models.CharField(max_length=50, verbose_name=u"Nome do Cartão")
    validade = models.CharField(max_length=7)
    vencimento = models.IntegerField(default=1)
    limite = models.FloatField(default=510)
    bandeira = models.ForeignKey(Bandeira, default=1)
    situacao = models.BooleanField(default=True, verbose_name=u"Situação")

    def __unicode__(self):
        return u'{nome:s}'.format(nome=self.nome)

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

        self.bestDayBuy()

        for compra in compras:

            if(compra.datacompra < self._dtBestDay
               and compra.parcelasRest() >= 0):
                soma += compra.valor
                print(compra, self._dtBestDay, compra.parcelasRest(), compra.qtparcelas, compra.parcelasPg())
            else:
                print(compra, self._dtBestDay, compra.parcelasRest(), compra.qtparcelas, compra.parcelasPg())

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
    #situacao.short_description = u'Situação'
    bestDayBuy.short_description = 'Melhor dia de Compra'
    proxFatura.short_description = 'Data da Prox. Fatura'
    parcialFatura.short_description = 'Parcial da Prox. Fatura'


class Compra(models.Model):
    cartao = models.ForeignKey(Cartao, related_name='compra')
    descricao = models.CharField(max_length=50, verbose_name=u"Descrição da Compra")
    valor = models.FloatField(default=5)
    qtparcelas = models.IntegerField(default=1)
    datacompra = models.DateField('Data da Compra')
    situacao = models.BooleanField(default=True, verbose_name=u"Situação")

    def __unicode__(self):
        return u"{descricao:s} data da compra: {datacompra:s}".format(descricao=self.descricao,
                                                                      datacompra=self.datacompra.strftime('%d/%m/%Y'))

    def parcelasPg(self):
        hoje = date.today()
        add = 0
        if(hoje.year > self.datacompra.year):
            add = hoje.year - self.datacompra.year
        parcpg = hoje.month - self.datacompra.month

        if(self.datacompra.day < self.cartao.bestDayBuy()):
            parcpg -= 1

        return parcpg+add*12

    def parcelasRest(self):
        return self.qtparcelas - self.parcelasPg()
