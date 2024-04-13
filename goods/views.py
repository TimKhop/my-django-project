from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Спорт Лайн - Каталог",
        "catalog_cart": [
            {
                "image": "deps/images/Велосипед_1.jpeg",
                "name": "Велосипед"
            },
            {
                "image": "deps/images/Мяч_5.jpeg",
                "name": "Мячи"
            },
            {
                "image": "deps/images/Кроссовки_2.jpeg",
                "name": "Кроссовки"
            },
            {
                "image": "deps/images/Тренажер_4.jpeg",
                "name": "Тренажеры"
            },
            {
                "image": 'deps/images/Спортивный инвентарь_3.jpeg',
                "name": "Спортивный инвентарь"
            },
        ]
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
