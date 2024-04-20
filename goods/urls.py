from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('search/', views.catalog_category, name='search'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('catalog/', views.catalog, name='catalog'),
    path('action/', views.action, name='action'),
    path('new_goods/', views.new_goods, name='new_goods'),
    path('category/<slug:category_slug>/', views.catalog_category, name='category')
]