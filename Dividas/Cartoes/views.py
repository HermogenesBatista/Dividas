# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from Cartoes.models import *

# Create your views here.
def index(request):
    return HttpResponse('Essa eh uma pagina de teste.')

def resultado(request, cartao_id):

    if(cartao_id == 'all'):
        c = Cartao.objects.all()
    else:
        c = [Cartao.objects.get(pk=cartao_id)]

    html = '''
    <!DOCTYPE>
    <html lang='pt-br'>
    <head>
        <meta charset='UTF-8'>
        <title>View Test</title>
    </head>
    <body>
        <table>
            <thead>
                <tr>
                    <td>Nome</td>
                    <td>Bandeira</td>
                    <td>Validade</td>
                    <td>Limite</td>
                    <td>Parcial da Fatura</td>
                    <td>Proxima Fatura</td>
                </tr>
            </thead>
            <tbody>'''

    for compra in c:
        linharesultado = '''
                <tr align='center'>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%.2f</td>
                    <td>%.2f</td>
                    <td>%s</td>
                </tr>''' %(compra.nome, compra.bandeira, compra.validade, compra.limite,
                           compra.parcialFatura(), compra.proxFatura().strftime('%d/%m/%Y'))

        html += linharesultado

    html +='''</tbody>
        </table>

    </body>
    </html>

    '''


    return HttpResponse(html)
