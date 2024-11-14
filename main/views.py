from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def news(request):
    news = News.objects.order_by('-date')
    return render(request, 'main/news.html', {'news': news})
