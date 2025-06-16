from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from basket.views import basket_remove, basket_clear, basket_buy, open_order, basket_add, basket_detail

urlpatterns = [
    path('', basket_detail, name='basket_detail'),

    path('remove/<str:product_type>/<int:product_id>/', basket_remove, name='basket_remove'),
    path('clear/', basket_clear, name='basket_clear'),
    path('buy/', basket_buy, name='basket_buy'),
    path('add/<str:product_type>/<int:product_id>/', basket_add, name='basket_add'),


    path('create_order/', open_order, name='order_open'),
]


