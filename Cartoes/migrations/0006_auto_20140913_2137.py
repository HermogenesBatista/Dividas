# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartoes', '0005_auto_20140910_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandeira',
            name='situacao',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartao',
            name='situacao',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='situacao',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
