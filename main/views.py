from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Спорт Лайн - Главная'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Спорт Лайн - О нас'
    }

    return render(request, 'main/about.html', context)