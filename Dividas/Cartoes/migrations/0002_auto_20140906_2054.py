# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=50)),
                ('qtparcelas', models.IntegerField(default=1)),
                ('datacompra', models.DateField(verbose_name=b'Data da Compra')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Cartoes',
            new_name='Cartao',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='cartao',
        ),
        migrations.DeleteModel(
            name='Compras',
        ),
        migrations.AddField(
            model_name='compra',
            name='cartao',
            field=models.ForeignKey(to='Cartoes.Cartao'),
            preserve_default=True,
        ),
    ]
