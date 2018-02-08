# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField

class Game(models.Model):
    game_title = models.CharField(max_length=150)
    gameImg0 = models.TextField()
    carouselCaptionHeader0 = HTMLField()
    carouselCaptionText0 = HTMLField()
    gameImg1 = models.TextField()
    carouselCaptionHeader1 = HTMLField()
    carouselCaptionText1 = HTMLField()
    gameImg2 = models.TextField()
    carouselCaptionHeader2 = HTMLField()
    carouselCaptionText2 = HTMLField()
    game_description = HTMLField()
    game_description_min = HTMLField()

    def __unicode__(self):
        return self.game_title

    def get_absolute_url(self):
        return "/games/%i/" % self.id
