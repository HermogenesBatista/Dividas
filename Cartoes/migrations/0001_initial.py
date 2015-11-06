# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cartoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('validade', models.CharField(max_length=7)),
                ('vencimento', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('qtparcelas', models.IntegerField(default=1)),
                ('datacompra', models.DateField(verbose_name=b'Data da Compra')),
                ('cartao', models.ForeignKey(to='Cartoes.Cartoes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
