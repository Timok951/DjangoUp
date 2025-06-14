from django import forms
from .models import Capacitor, Category, Producer, Product_type, Resistor, Chip, User, Order, Order_Capacitor, Order_Resistor, Order_Chip

class CapacitorForm(forms.ModelForm):
    class Meta:
        model=Capacitor
        fields = ['name', 'description', 'price', 'capacity', 'photo', 'is_exist', 'category', 'producer', 'product_type']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['name', 'description']

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name', 'description']

class Product_typeForm(forms.ModelForm):
    class Meta:
        model = Product_type
        fields = ['name', 'discount']

class ResistorForm(forms.ModelForm):
    class Meta:
        model = Resistor
        fields = ['name', 'description', 'price', 'resist', 'photo', 'is_exists', 'category', 'producer', 'product_type']

class ChipForm(forms.ModelForm):
    class Meta:
        model = Chip
        fields = ['name', 'description', 'price', 'photo', 'is_exists', 'category', 'producer', 'product_type']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nick', 'phone', 'email', 'password']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user']

class Order_CapacitorForm(forms.ModelForm):
    class Meta:
        model = Order_Capacitor
        fields = ['capacitor', 'amount', 'order']

class Order_ResistorForm(forms.ModelForm):
    class Meta:
        model = Order_Resistor
        fields = ['resistor', 'amount', 'order']

class Order_ChipForm(forms.ModelForm):
    class Meta:
        model = Order_Chip
        fields = ['chip', 'amount', 'order']


class LoginForm(AuthenticationForm):
    username = Forms.Charfield(
        label="Логин пользователя",
        
    )
