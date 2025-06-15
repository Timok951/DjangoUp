from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from basket.views import basket_remove, basket_clear, basket_buy, open_order

urlpatterns = [
    path('', include('shop.urls')),
    path('basket/', include('basket.urls')),

    # Эти маршруты относятся к корзине напрямую
    path('basket/remove/<str:product_type>/<int:product_id>/', basket_remove, name='basket_remove'),
    path('basket/clear/', basket_clear, name='basket_clear'),
    path('basket/buy/', basket_buy, name='basket_buy'),

    # Оформление заказа
    path('basket/create_order/', open_order, name='order_open'),
]


