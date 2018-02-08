# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

class Message(models.Model):
    title_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    message_text = HTMLField()

    def __unicode__(self):
        return self.title_text

    def get_absolute_url(self):
        return "/news/%i/" % self.id
