from django.shortcuts import render
from goods.models import Categories, Products

def index(request):
    categories = Categories.objects.all()  # Использование модели Categories
    action = Products.objects.filter(discount__gt=0).order_by('?')[:3]
    new_goods = Products.objects.filter(new="Да").order_by('?')[:3]
    context = {
        'title': 'Спорт Лайн - Главная',
        'categories': categories,
        'action': action,
        'new_goods': new_goods,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Спорт Лайн - О нас'
    }
    return render(request, 'main/about.html', context)