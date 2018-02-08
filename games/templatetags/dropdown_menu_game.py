# -*- coding:utf-8 -*-

import random
from django import template
from games.models import Game

register = template.Library() 
# регистрируем наш тег, который будет выводить шаблон dropdown_menu_game
@register.inclusion_tag("dropdown_menu_game.html")
def show_dropdown_menu():
    new_game = Game.objects.values('id','game_title').order_by("id")
    return {'new_game': new_game}

@register.inclusion_tag("carousel_game.html")
def show_carousel():
    new_game = Game.objects.values('id','game_title','gameImg0','gameImg1','gameImg2','carouselCaptionHeader0','carouselCaptionHeader1','carouselCaptionHeader2','carouselCaptionText0','carouselCaptionText1','carouselCaptionText2').order_by("id")
    rndGame = random.choice(new_game)
    return {'game': rndGame}