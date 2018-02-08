# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20150929_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameImg0',
            field=models.FilePathField(verbose_name=b'/media/uploads'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameImg1',
            field=models.FilePathField(verbose_name=b'/media/uploads'),
        ),
        migrations.AlterField(
            model_name='game',
            name='gameImg2',
            field=models.FilePathField(verbose_name=b'/media/uploads'),
        ),
    ]
