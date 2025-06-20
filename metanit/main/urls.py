from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('location/', location, name='location'),
    path('categories/', categories, name='categories'),
    path('all-products/', all_products, name='all_products'),
    path('cart/', cart, name='cart'),

    path('capacitor/', CapacitorListView.as_view(), name='capacitor_list'),
    path('capacitor/<int:pk>/', CapacitorDetailView.as_view(), name='capacitor_detail'),
    path('capacitor/create/', CapacitorCreateView.as_view(), name='capacitor_create'),
    path('capacitor/<int:pk>/update/', CapacitorUpdateView.as_view(), name='capacitor_update'),
    path('capacitor/<int:pk>/delete/', CapacitorDeleteView.as_view(), name='capacitor_confirm_delete'),

    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_confirm_delete'),

    path('producer/', ProducerListView.as_view(), name='producer_list'),
    path('producer/<int:pk>/', ProducerDetailView.as_view(), name='producer_detail'),
    path('producer/create/', ProducerCreateView.as_view(), name='producer_create'),
    path('producer/<int:pk>/update/', ProducerUpdateView.as_view(), name='producer_update'),
    path('producer/<int:pk>/delete/', ProducerDeleteView.as_view(), name='producer_confirm_delete'),

    path('product_type/', Product_typeListView.as_view(), name='product_type_list'),
    path('product_type/<int:pk>/', Product_typeDetailView.as_view(), name='product_type_detail'),
    path('product_type/create/', Product_typeCreateView.as_view(), name='product_type_create'),
    path('product_type/<int:pk>/update/', Product_typeUpdateView.as_view(), name='product_type_update'),
    path('product_type/<int:pk>/delete/', Product_typeDeleteView.as_view(), name='product_type_confirm_delete'),

    path('chip/', ChipListView.as_view(), name='chip_list'),
    path('chip/<int:pk>/', ChipDetailView.as_view(), name='chip_detail'),
    path('chip/create/', ChipCreateView.as_view(), name='chip_create'),
    path('chip/<int:pk>/update/', ChipUpdateView.as_view(), name='chip_update'),
    path('chip/<int:pk>/delete/', ChipDeleteView.as_view(), name='chip_confirm_delete'),

    path('login/', login_user, name='login'),
    path('registration/', registration_user, name='registration_page'),
    path('logout/', logout_user, name='logout_page'),

]
