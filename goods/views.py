from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products
from goods.utils import q_search  # Обновленный импорт
from django.db.models import Case, When, IntegerField



def catalog(request):
    catalog = Categories.objects.all()  # Использование модели Categories
    context = {"title": "Спорт Лайн - Каталог", "catalog": catalog}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


def action(request):
    # Получаем параметр для пагинации и сортировки
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')

    # Фильтруем товары по акциям
    catalog_cart_action = Products.objects.filter(~Q(discount=0.00))
    
    # Добавляем аннотацию, чтобы разделить товары на те, что в наличии и те, что нет
    catalog_cart_action = catalog_cart_action.annotate(
        in_stock=Case(
            When(quantity__gt=0, then=1),  # Если товар в наличии
            default=0,  # Если товар не в наличии
            output_field=IntegerField(),
        )
    )

    # Применяем сортировку: сначала по наличию, затем по цене, если указано
    if order_by == 'price':
        catalog_cart_action = catalog_cart_action.order_by('-in_stock', 'price')  # От дешевых к дорогим
    elif order_by == '-price':
        catalog_cart_action = catalog_cart_action.order_by('-in_stock', '-price')  # От дорогих к дешевым
    else:
        # Если нет сортировки, отображаем сначала товары в наличии, затем все остальные
        catalog_cart_action = catalog_cart_action.order_by('-in_stock')

    # Применяем пагинацию
    paginator = Paginator(catalog_cart_action, 9)  # 9 товаров на странице
    current_page = paginator.page(int(page))
    
    # Рендерим шаблон с пагинацией и сортировкой
    return render(
        request,
        "goods/action.html",
        {
            "title": "Спорт Лайн - Акции", 
            "catalog_cart_action": current_page,
            "order_by": order_by,
        },
    )

def new_goods(request):
    # Получаем параметр сортировки из запроса, по умолчанию сортируем по наличию
    order_by = request.GET.get('order_by', 'default')

    # Фильтруем товары, чтобы показать только новинки
    catalog_cart_new_goods = Products.objects.filter(new="Да")

    # Добавляем признак, чтобы разделить товары в наличии и те, которых нет
    catalog_cart_new_goods = catalog_cart_new_goods.annotate(
        in_stock=Case(
            When(quantity__gt=0, then=1),  # Если количество больше 0, это в наличии
            default=0,  # Если количество 0, это не в наличии
            output_field=IntegerField(),
        )
    )

    # Применяем сортировку: сначала по наличию, затем по цене, если указано
    if order_by == 'price':
        catalog_cart_new_goods = catalog_cart_new_goods.order_by('-in_stock', 'price')  # От дешевых к дорогим
    elif order_by == '-price':
        catalog_cart_new_goods = catalog_cart_new_goods.order_by('-in_stock', '-price')  # От дорогих к дешевым
    else:
        # Если сортировка не указана, сортируем только по наличию
        catalog_cart_new_goods = catalog_cart_new_goods.order_by('-in_stock')

    # Передаем контекст в шаблон
    context = {
        "title": "Спорт Лайн - Новинки",
        "catalog_cart_new_goods": catalog_cart_new_goods,
        "order_by": order_by,
    }

    # Рендерим шаблон с контекстом
    return render(request, "goods/new_goods.html", context)



def catalog_category(request, category_slug=None):
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if query:
        products = q_search(query)
        category = None  # Поскольку мы ищем товары по запросу, категория не определена
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        products = Products.objects.filter(category=category)  # Получение товаров выбранной категории

    if on_sale:
        products = products.filter(discount__gt=0)

    # Добавляем поле, чтобы сначала были товары в наличии, затем другие критерии
    products = products.annotate(
        in_stock=Case(
            When(quantity__gt=0, then=1),  # Товары в наличии
            default=0,  # Товары, которых нет в наличии
            output_field=IntegerField(),
        )
    )

    # Сначала товары в наличии, затем дополнительные критерии
    if order_by and order_by != "default":
        products = products.order_by("-in_stock", order_by)  # Гарантируем наличие как приоритетное условие
    else:
        products = products.order_by("-in_stock")  # По умолчанию, сортируем по наличию

    catalog = Categories.objects.all()  # Используем модель Categories

    title = f"Спорт Лайн - Каталог - {category.name}" if category else "Спорт Лайн - Результаты поиска"
    return render(
        request,
        "goods/catalog_category.html",
        {
            "title": title,
            "products": products,
            "category": category,
            "catalog": catalog,
        },
    )