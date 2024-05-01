from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('qr_code/<int:order_id>/', views.qr_code, name='qr_code'),
]