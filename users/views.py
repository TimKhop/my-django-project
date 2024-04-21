from calendar import c
from django.shortcuts import render

def login(request):
    context = {
        'title': 'Спорт Лайн - Авторизация'
    }
    return render(request, '', context)

def registration(request):
    context = {
        'title': 'Спорт Лайн - Регистрация'
    }
    return render(request, '', context)

def profile(request):
    context = {
        'title': 'Спорт Лайн - Профиль'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...