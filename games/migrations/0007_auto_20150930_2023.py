# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20150929_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='carouselCaptionHeader0',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 29, 399186, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='carouselCaptionHeader1',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 33, 853661, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='carouselCaptionHeader2',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 38, 165714, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='carouselCaptionText0',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 42, 39520, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='carouselCaptionText1',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 46, 32001, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='carouselCaptionText2',
            field=tinymce.models.HTMLField(default=datetime.datetime(2015, 9, 30, 17, 23, 50, 910632, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
