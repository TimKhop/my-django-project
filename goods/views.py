# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render

from goods.models import Categories, Products
from django.db.models import Q


def catalog(request):

    catalog = Categories.objects.all()

    context = {
        "title": "Спорт Лайн - Каталог",
        "catalog": catalog,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug) # type: ignore

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context)


def action(request):

    catalog_cart_action = Products.objects.filter(~Q(discount=0.00))
    context = {
        "title": "Спорт Лайн - Акции",
        "catalog_cart_action": catalog_cart_action,
    }

    return render(request, "goods/action.html", context)


def new_goods(request):

    catalog_cart_new_goods = Products.objects.filter(new="Да")
    context = {
        "title": "Спорт Лайн - Акции",
        "catalog_cart_new_goods": catalog_cart_new_goods,
    }

    return render(request, "goods/new_goods.html", context)


def catalog_bicycle(request):

    catalog_cart_bicycle = Products.objects.filter(category__name="Велосипеды")
    context = {
        "title": "Спорт Лайн - Каталог - Велосипеды",
        "catalog_cart_bicycle": catalog_cart_bicycle,
    }

    return render(request, "goods/catalog_bicycle.html", context)


def balls(request):

    catalog_cart_balls = Products.objects.filter(category__name="Мячи")
    context = {
        "title": "Спорт Лайн - Каталог - Мячи",
        "catalog_cart_balls": catalog_cart_balls,
    }

    return render(request, "goods/balls.html", context)


def sneakers(request):

    catalog_cart_sneakers = Products.objects.filter(category__name="Кроссовки")
    context = {
        "title": "Спорт Лайн - Каталог - Кроссовки",
        "catalog_cart_sneakers": catalog_cart_sneakers,
    }

    return render(request, "goods/sneakers.html", context)


def trainer(request):

    catalog_cart_trainer = Products.objects.filter(category__name="Тренажеры")
    context = {
        "title": "Спорт Лайн - Каталог - Тренажеры",
        "catalog_cart_trainer": catalog_cart_trainer,
    }

    return render(request, "goods/trainer.html", context)


def sports_equipment(request):

    catalog_cart_sports_equipment = Products.objects.filter(category__name="Спортивный инвентарь")
    context = {
        "title": "Спорт Лайн - Каталог - Спортивный инвентарь",
        "catalog_cart_sports_equipment": catalog_cart_sports_equipment,
    }

    return render(request, "goods/sports_equipment.html", context)
