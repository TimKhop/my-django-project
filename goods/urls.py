from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('catalog/', views.catalog, name='catalog'),
    path('action/', views.action, name='action'),
    path('new_goods/', views.new_goods, name='new_goods'),
    path('catalog_bicycle/', views.catalog_bicycle, name='catalog_bicycle'),
    path('balls/', views.balls, name='balls'),
    path('sneakers/', views.sneakers, name='sneakers'),
    path('trainer/', views.trainer, name='trainer'),
    path('sports_equipment/', views.sports_equipment, name='sports_equipment'),

    path('/products/<slug:category_slug>', views.products_by_category, name='category'),
]