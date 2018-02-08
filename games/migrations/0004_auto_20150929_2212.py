# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20150929_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameImg0',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameImg1',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameImg2',
            field=models.URLField(),
        ),
    ]
