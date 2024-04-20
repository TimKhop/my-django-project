from pickle import GET
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Products  # Обновленный импорт


def catalog(request):
    catalog = Categories.objects.all()  # Использование модели Categories
    context = {"title": "Спорт Лайн - Каталог", "catalog": catalog}
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    return render(request, "goods/product.html", {"product": product})


def action(request):
    page = request.GET.get('page', 1)
    catalog_cart_action = Products.objects.filter(~Q(discount=0.00))
    paginator = Paginator(catalog_cart_action, 9)
    current_page = paginator.page(int(page))
    return render(
        request,
        "goods/action.html",
        {
            "title": "Спорт Лайн - Акции", 
            "catalog_cart_action": current_page
        },
    )


def new_goods(request):
    catalog_cart_new_goods = Products.objects.filter(new="Да")
    return render(
        request,
        "goods/new_goods.html",
        {
            "title": "Спорт Лайн - Новинки",
            "catalog_cart_new_goods": catalog_cart_new_goods,
        },
    )


def catalog_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Products.objects.filter(category=category)
    catalog = Categories.objects.all()  # Использование модели Categories
    return render(
        request,
        "goods/catalog_category.html",
        {
            "title": f"Спорт Лайн - Каталог - {category.name}",
            "products": products,
            "category": category,
            "catalog": catalog,
        },
    )
