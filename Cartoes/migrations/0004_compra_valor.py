# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartoes', '0003_cartao_limite'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='valor',
            field=models.FloatField(default=5),
            preserve_default=True,
        ),
    ]
