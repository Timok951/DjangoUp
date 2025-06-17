from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    CapacitorViewSet, ResistorViewSet, ChipViewSet,
    ProducerViewSet, CategoryViewSet, ProductTypeViewSet,
    UserViewSet, OrderViewSet,
    OrderCapacitorViewSet, OrderResistorViewSet, OrderChipViewSet
)

router = SimpleRouter()
router.register('capacitor', CapacitorViewSet, basename='capacitor')
router.register('resistor', ResistorViewSet, basename='resistor')
router.register('chip', ChipViewSet, basename='chip')
router.register('producer', ProducerViewSet, basename='producer')
router.register('category', CategoryViewSet, basename='category')
router.register('product_type', ProductTypeViewSet, basename='product_type')
router.register('user', UserViewSet, basename='user')
router.register('order', OrderViewSet, basename='order')
router.register('order_capacitor', OrderCapacitorViewSet, basename='order_capacitor')
router.register('order_resistor', OrderResistorViewSet, basename='order_resistor')
router.register('order_chip', OrderChipViewSet, basename='order_chip')

urlpatterns = router.urls
