from django.shortcuts import redirect, render
from goods.models import Categories, Products
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

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


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Получаем данные из POST-запроса
        if form.is_valid():  # Проверка валидации формы
            # Получение данных из формы
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка электронного письма
            send_contact_email(name, email, message)

            # Сообщение об успешной отправке
            messages.success(request, "Ваше сообщение было отправлено успешно!")
            return redirect('main:index')  # Перенаправление после успешной отправки
    else:
        form = ContactForm()  # Если запрос GET, создаем пустую форму
    
    return render(request, 'main/contact_form.html', {'form': form})  # Передаем форму в шаблон

def handle_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Получаем данные из формы
        if form.is_valid():
            # Логика обработки данных формы (например, отправка электронной почты)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Отправка письма
            send_contact_email(name, email, message)

            messages.success(request, "Ваше сообщение было отправлено успешно!")
            return redirect('main:index')  # Возврат на главную страницу
    else:
        form = ContactForm()  # Если запрос не POST, создаем пустую форму
    
    return render(request, 'main/contact_form.html', {'form': form})