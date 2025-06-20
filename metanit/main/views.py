from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def location(request):
    return render(request, 'main/location.html')

def products(request):
    return render(request, 'main/products.html')

def categories(request):
    return render(request, 'main/categories.html')

from django.shortcuts import render
from .models import Chip, Capacitor, Resistor

def all_products(request):
    chips = Chip.objects.filter(is_exists=True)
    capacitors = Capacitor.objects.filter(is_exist=True)
    resistors = Resistor.objects.filter(is_exists=True)

    context = {
        'chips': chips,
        'capacitors': capacitors,
        'resistors': resistors,
    }
    return render(request, 'main/all_products.html', context)


def cart(request):
    return render(request, 'main/cart.html')

class CapacitorListView(ListView):
    model = Capacitor
    template_name = 'capacitor/capacitor_list.html'
    context_object_name = 'capacitor'

class CapacitorDetailView(DetailView):
    model = Capacitor
    template_name='capacitor/capacitor_detail.html'
    context_object_name = 'capacitor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class CapacitorCreateView(CreateView):
    model = Capacitor
    form_class = CapacitorForm
    template_name = 'capacitor/capacitor_form.html'
    success_url = reverse_lazy('capacitor_list')

class CapacitorUpdateView(UpdateView):
    model = Capacitor
    form_class = CapacitorForm
    template_name = 'capacitor/capacitor_form.html'
    success_url = reverse_lazy('capacitor_list')

class CapacitorDeleteView(DeleteView):
    model = Capacitor
    template_name = 'capacitor/capacitor_confirm_delete.html'  
    success_url = reverse_lazy ('capacitor_list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'category'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class ProducerListView(ListView):
    model = Producer
    template_name = 'producer/producer_list.html'
    context_object_name = 'producer'

class ProducerDetailView(DetailView):
    model = Producer
    template_name = 'producer/producer_detail.html'
    context_object_name = 'producer'

class ProducerCreateView(CreateView):
    model = Producer
    form_class = ProducerForm
    template_name = 'producer/producer_form.html'
    success_url = reverse_lazy('producer_list')

class ProducerUpdateView(UpdateView):
    model = Producer
    form_class = ProducerForm
    template_name = 'producer/producer_form.html'
    success_url = reverse_lazy('producer_list')

class ProducerDeleteView(DeleteView):
    model = Producer
    template_name = 'producer/producer_confirm_delete.html'
    success_url = reverse_lazy('producer_list')

class Product_typeListView(ListView):
    model = Product_type
    template_name = 'product_type/product_type_list.html'
    context_object_name = 'product_type'

class Product_typeDetailView(DetailView):
    model = Product_type
    template_name = 'product_type/product_type_detail.html'
    context_object_name = 'product_type'

class Product_typeCreateView(CreateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product_type/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class Product_typeUpdateView(UpdateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product_type/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class Product_typeDeleteView(DeleteView):
    model = Product_type
    template_name = 'product_type/product_type_confirm_delete.html'
    success_url = reverse_lazy('product_type_list')

class ResistorListView(ListView):
    model = Resistor
    template_name = 'resistor/resistor_list.html'
    context_object_name = 'resistor' 

class ResistorDetailView(DetailView):
    model = Resistor
    template_name = 'resistor/resistor_detail.html'
    context_object_name = 'resistor'

class ResistorCreateView(CreateView):
    model =ResistorForm
    template_name = 'resistor/resistor_form.html'
    context_object_name = 'resistor'

class ResistorUpdateView(UpdateView):
    model = Resistor 
    form_class = ResistorForm
    template_name = 'resistor/resistor_form.html'
    success_url = reverse_lazy('resistor_list')

class ResistorDeleteView(DeleteView):
    model = Resistor
    template_name = 'resistor/resistor_confirm_delete.html'
    success_url = reverse_lazy('resistor_list')

class ChipListView(ListView):
    model = Chip
    template_name = 'chip/chip_list.html'
    context_object_name = 'chip'

class ChipDetailView(DetailView):
    model =Chip
    template_name = 'chip/chip_detail.html'
    context_object_name = 'chip'

class ChipCreateView(CreateView):
    model = Chip
    form_class = ChipForm
    template_name = 'chip/chip_form.html'
    context_object_name = 'chip'
    success_url = reverse_lazy('chip_list')

class ChipUpdateView(UpdateView):
    model = Chip
    form_class = ChipForm
    template_name = 'chip/chip_form.html'
    context_object_name = 'chip'
    success_url = reverse_lazy('chip_list')

class ChipDeleteView(DeleteView):
    model = Chip
    template_name = 'chip/chip_confirm_delete.html'
    success_url = reverse_lazy('chip_list')

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'user'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/user.form'
    success_url = reverse_lazy('user_list')

class UserDelete(DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'order'

class OrderDetailVeiw(DetailView):
    model = Order
    template_name = 'order/order_form.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list.html')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

class Order_CapacitorListView(ListView):
    model = Order_Capacitor
    template_name = 'order_capacitor/order_capacitor_list.html'
    context_object_name = 'order_capacitor'

class Order_CapacitorDetailVeiw(DetailView):
    model = Order_Capacitor
    template_name = 'order_capacitor/order_capacitor_form.html'
    context_object_name = 'order_capacitor'

class Order_CapacitorCreateView(CreateView):
    model = Order_Capacitor
    form_class = Order_CapacitorForm
    template_name = 'order_capacitor/order_capacitor_form.html'
    success_url = reverse_lazy('order_capacitor_list.html')

class Order_CapacitorUpdateView(UpdateView):
    model = Order_Capacitor
    form_class = Order_CapacitorForm
    template_name = 'order_capacitor/order_capacitor_form.html'
    success_url = reverse_lazy('order_capacitor_list')

class Order_CapacitorDeleteView(DeleteView):
    model = Order
    template_name = 'order_capacitor/order_capacitor_confirm_delete.html'
    success_url = reverse_lazy('order_capacitor_list')

class Order_ResistorListView(ListView):
    model = Order_Resistor
    template_name = 'order_resistor/order_resistor_list.html'
    context_object_name = 'order_resistor'

class Order_ResistorDetailVeiw(DetailView):
    model = Order_Resistor
    template_name = 'order_resistor/order_resistor_form.html'
    context_object_name = 'order_resistor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class Order_ResistorCreateView(CreateView):
    model = Order_Resistor
    form_class = Order_ResistorForm
    template_name = 'order_capacitor/order_resistor_form.html'
    success_url = reverse_lazy('order_resistor_list.html')

class Order_ResistorUpdateView(UpdateView):
    model = Order_Resistor
    form_class = Order_ResistorForm
    template_name = 'order_resistor/order_resistor_form.html'
    success_url = reverse_lazy('order_resistor_list')

class Order_ResistorDeleteView(DeleteView):
    model = Order
    template_name = 'order_resistor/order_resistor_confirm_delete.html'
    success_url = reverse_lazy('order_resistor_list')

class Order_ChipListView(ListView):
    model = Order_Chip
    template_name = 'order_chip/order_chip_list.html'
    context_object_name = 'order_resistor'

class Order_ChipDetailVeiw(DetailView):
    model = Order_Chip
    template_name = 'order_chip/order_chip_form.html'
    context_object_name = 'order_chip'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class Order_ChipCreateView(CreateView):
    model = Order_Chip
    form_class = Order_ChipForm
    template_name = 'order_chip/order_chip_form.html'
    success_url = reverse_lazy('order_chip_list.html')

class Order_ChipUpdateView(UpdateView):
    model = Order_ChipForm
    form_class = Order_ChipForm
    template_name = 'order_chip/order_chip_form.html'
    success_url = reverse_lazy('order_chip_list')

class Order_ChipDeleteView(DeleteView):
    model = Order
    template_name = 'order_chip/order_chip_confirm_delete.html'
    success_url = reverse_lazy('order_chip_list')

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm

def login_user(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'capacitor_list')
    return render(request, 'auth/login.html', {'form': form})

def registration_user(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('capacitor_list')
    return render(request, 'auth/register.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('capacitor_list')


