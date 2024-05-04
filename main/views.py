from django.http import JsonResponse
from django.shortcuts import redirect, render
from goods.models import Categories, Products
from users.forms import UserRegistrationForm
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    categories = Categories.objects.all()  # Использование модели Categories
    action = Products.objects.filter(discount__gt=0, quantity__gt=0).order_by('?')[:3]
    new_goods = Products.objects.filter(new="Да", quantity__gt=0).order_by('?')[:3]
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



def send_contact_email(name, email, message):
    subject = "Сообщение с вашего сайта"
    body = f"Сообщение от {name} ({email}):\n\n{message}"
    from_email = 'TiMe2003R@yandex.ru'  # Адрес электронной почты отправителя
    to_email = 'TiMe2003R@yandex.ru'  # Адрес электронной почты, куда придет письмо
    
    send_mail(
        subject,
        body,
        from_email, 
        [to_email], 
        fail_silently=False
    )


# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)  # Получаем данные из POST-запроса
#         if form.is_valid():  # Проверка валидации формы
#             # Получение данных из формы
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Отправка электронного письма
#             send_contact_email(name, email, message)

#             # Сообщение об успешной отправке
#             messages.success(request, "Ваше сообщение было отправлено успешно!")
#             return redirect('main:index')  # Перенаправление после успешной отправки
#     else:
#         form = ContactForm()  # Если запрос GET, создаем пустую форму
    
#     return render(request, 'main/contact_form.html', {'form': form})  # Передаем форму в шаблон

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Отправка письма
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_contact_email(name, email, message)

            messages.success(request, "Сообщение успешно отправлено!")
            return redirect('main:index')  # Перенаправление на главную
    else:
        form = ContactForm()
    return render(request, 'main/contact_form.html', {'form': form})

# def handle_contact_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)  # Получаем данные из формы
#         if form.is_valid():
#             # Логика обработки данных формы (например, отправка электронной почты)
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']

#             # Отправка письма
#             send_contact_email(name, email, message)

#             messages.success(request, "Ваше сообщение было отправлено успешно!")
#             return redirect('main:index')  # Возврат на главную страницу
#     else:
#         form = ContactForm()  # Если запрос не POST, создаем пустую форму
    
#     return render(request, 'main/contact_form.html', {'form': form})

def handle_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_contact_email(name, email, message)
            return JsonResponse({'success': True})  # Отправляем успех в ответ на AJAX-запрос
        else:
            # Отправляем ошибки в формате JSON
            errors = {field: error for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ContactForm()  # Создаем новую форму для GET-запроса
        return render(request, 'main/contact_form.html', {'form': form})
    