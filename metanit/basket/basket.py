from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from main.models import Order, Order_Capacitor, Order_Resistor, Order_Chip
from shop.models import Chip, Resistor, Capacitor
from .basket import Basket
from .forms import BasketAddProductForm, OrderForm

# Детали корзины
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})

# Удаление из корзины
def basket_remove(request, product_type, product_id):
    basket = Basket(request)
    
    model = {'chip': Chip, 'resistor': Resistor, 'capacitor': Capacitor}.get(product_type)
    if not model:
        return redirect('basket_detail')
    
    product = get_object_or_404(model, pk=product_id)
    basket.remove(product_type, product)
    return redirect('basket_detail')

# Очистка корзины
def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

# Добавление товара в корзину
@require_POST
def basket_add(request, product_type, product_id):
    basket = Basket(request)
    
    model = {'chip': Chip, 'resistor': Resistor, 'capacitor': Capacitor}.get(product_type)
    if not model:
        return redirect('basket_detail')

    product = get_object_or_404(model, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(
            product=product,
            count=form.cleaned_data['count'],
            update_count=form.cleaned_data['reload'],
            product_type=product_type
        )
    return redirect('basket_detail')

# Страница оформления заказа
@login_required
def open_order(request):
    return render(request, 'order/order_form.html', {'form_order': OrderForm()})

# Покупка корзины → создание заказа
@login_required
def basket_buy(request):
    basket = Basket(request)
    if len(basket) <= 0:
        return redirect('basket_detail')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in basket:
                product = item['product']
                count = item['count']
                type_ = item['type']

                if type_ == 'chip':
                    Order_Chip.objects.create(order=order, chip=product, amount=count)
                elif type_ == 'resistor':
                    Order_Resistor.objects.create(order=order, resistor=product, amount=count)
                elif type_ == 'capacitor':
                    Order_Capacitor.objects.create(order=order, capacitor=product, amount=count)

            basket.clear()
            return redirect('basket_detail')
    else:
        form = OrderForm()

    return render(request, 'order/order_form.html', {'form_order': form})
