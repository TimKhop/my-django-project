from django.shortcuts import render
from goods.models import Categories

def index(request):
    categories = Categories.objects.all()  # Использование модели Categories
    context = {
        'title': 'Спорт Лайн - Главная',
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Спорт Лайн - О нас'
    }
    return render(request, 'main/about.html', context)