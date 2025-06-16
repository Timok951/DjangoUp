from django import forms
from .models import Capacitor, Category, Producer, Product_type, Resistor, Chip, Order, Order_Capacitor, Order_Resistor, Order_Chip
from .models import User


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

from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    nick = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=2
    )
    email = forms.EmailField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    phone = forms.CharField(
        label='Телефон',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['nick', 'email', 'phone', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
