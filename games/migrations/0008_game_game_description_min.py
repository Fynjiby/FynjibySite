# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20150930_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_description_min',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 10, 5, 19, 33, 30, 736283, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
