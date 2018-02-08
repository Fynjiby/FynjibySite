# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gameImg0',
            field=models.ImageField(default=1, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='gameImg1',
            field=models.ImageField(default=datetime.datetime(2015, 9, 29, 18, 58, 47, 572226, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='gameImg2',
            field=models.ImageField(default=datetime.datetime(2015, 9, 29, 18, 59, 4, 647834, tzinfo=utc), upload_to=b''),
            preserve_default=False,
        ),
    ]
