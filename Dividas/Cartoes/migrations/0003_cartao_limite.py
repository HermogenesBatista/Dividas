# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cartoes', '0002_auto_20140906_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartao',
            name='limite',
            field=models.FloatField(default=510),
            preserve_default=True,
        ),
    ]
