from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse


from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                return HttpResponseRedirect(reverse('main:index'))
        else:
            # Возвращаем страницу, которая содержит модальное окно, с контекстом, чтобы показать ошибки
            context = {
                'form': form,
            }
            return render(request, 'main/index.html', context)  # Шаблон, который содержит модальное окно

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированны и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
        else:
            # Возвращаем страницу, которая содержит модальное окно, с контекстом, чтобы показать ошибки
            context = {
                'form': form
            }
            return render(request, 'main/index.html', context)  # Шаблон, который содержит модальное окно

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f" Профиль успешно обновлен ")
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            # Возвращаем страницу, которая содержит модальное окно, с контекстом, чтобы показать ошибки
            context = {
                'form': form
            }
    else:
        form = ProfileForm(instance=request.user)

    context = {
        "title": "Спорт Лайн - Профиль", 
        'form': form
    }
    return render(request, 'users/profile.html', context)  # Шаблон, который содержит модальное окно

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

def my_orders(request):
    context = {
        "title": "Спорт Лайн - Мои заказы", 
        }
    return render(request, "users/my_orders.html", context)

def users_cart(request):
    context = {
        "title": "Спорт Лайн - Корзина", 
        }
    return render(request, "users/users_cart.html", context)
    