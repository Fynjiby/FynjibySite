# -*- coding:utf-8 -*-

from django import template
from news.models import Message

register = template.Library() 

@register.inclusion_tag("news_list.html")
def show_news_list7():
    new_messages = Message.objects.values('id','title_text','pub_date','message_text').order_by("-pub_date")[:7]
    return {'new_messages': new_messages}