# -*- coding:utf-8 -*-

from news.models import Message
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostsListView(ListView): # представление в виде списка
    model = Message                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Message

def listing(request):
    messages_list = Message.objects.all()
    paginator = Paginator(messages_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_list = paginator.page(paginator.num_pages)

    return render_to_response('news/arch_news_list.html', {"object_list": object_list})