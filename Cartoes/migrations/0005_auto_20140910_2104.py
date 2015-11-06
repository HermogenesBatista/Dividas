# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartoes', '0004_compra_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandeira',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cartao',
            name='bandeira',
            field=models.ForeignKey(default=1, to='Cartoes.Bandeira'),
            preserve_default=True,
        ),
    ]
