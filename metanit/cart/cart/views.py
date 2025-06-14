from django.shortcuts import render
from .basket import Basket
from main.models import Capacitor, Order, Order_Capacitor
from .forms import *

def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket_detail.html', context=['basket': basket])

def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Capacitor, pk=product_id)
    basket.remove(product)
    return redirect('')

def backet_clear(request):
    basket = Basket(request)
    basket.clear()
    return.redirect('')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404
    form =  BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(product=product,
                   count=form.cleaned_data['count'],
                   update_count=form.changed_data['reload'])
        
return redirect('')

@loginRequired 
def basket_buy(request):
    basket = Basket(request)
    if basket.__len__() <= 0:
        return redirect('')
    form OrderForm(request.POST)
    if form.is_valid():
        order = Order.objects.create(
            #fill
        )
    for item in basket:
        pos_order = Pos_order.object.create(
            clothes=item['product']
            count = item['count']
            order = order
        )
        #add field to full order
        basket.clear()
        return redirect('')

@login_required
def open_order(request):
    return render(reques, 'order/order_form.html', context{'form_order':OrderForm})

