# -*- coding:utf-8 -*-

from games.models import Game
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Game                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Game