from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products
from goods.utils import q_search  # Обновленный импорт


def catalog(request):
    catalog = Categories.objects.all()  # Использование модели Categories
    context = {"title": "Спорт Лайн - Каталог", "catalog": catalog}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


def action(request):
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'default')
    
    catalog_cart_action = Products.objects.filter(~Q(discount=0.00))
    
    if order_by == 'price':
        catalog_cart_action = catalog_cart_action.order_by('price')
    elif order_by == '-price':
        catalog_cart_action = catalog_cart_action.order_by('-price')
    
    paginator = Paginator(catalog_cart_action, 9)
    current_page = paginator.page(int(page))
    
    return render(
        request,
        "goods/action.html",
        {
            "title": "Спорт Лайн - Акции", 
            "catalog_cart_action": current_page,
            "order_by": order_by
        },
    )


def new_goods(request):
    order_by = request.GET.get('order_by', 'default')

    catalog_cart_new_goods = Products.objects.filter(new="Да")

    if order_by == 'price':
        catalog_cart_new_goods = catalog_cart_new_goods.order_by('price')
    elif order_by == '-price':
        catalog_cart_new_goods = catalog_cart_new_goods.order_by('-price')

    return render(
        request,
        "goods/new_goods.html",
        {
            "title": "Спорт Лайн - Новинки",
            "catalog_cart_new_goods": catalog_cart_new_goods,
            "order_by": order_by,
        },
    )


def catalog_category(request, category_slug=None):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if query:
        products = q_search(query)
        category = None  # Поскольку мы ищем товары по запросу, категория не определена
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        products = Products.objects.filter(category=category)  # Получение товаров выбранной категории

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    catalog = Categories.objects.all()  # Использование модели Categories

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