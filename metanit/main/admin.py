from django.contrib import admin
from .models import *

# Register your models here.
# Перейдем в файлик admin.py и зарегистрируем модели без каких любо настроек визуальности.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    pass

@admin.register(Product_type)
class Product_typeAdmin(admin.ModelAdmin):
    pass

@admin.register(Capacitor)
class CapacitorAdmin(admin.ModelAdmin):
    pass

@admin.register(Resistor)
class ResistorAdmin(admin.ModelAdmin):
    pass

@admin.register(Chip)
class ChipAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('nick', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('nick', 'password')}),
        ('Личная информация', {'fields': ('phone', 'email')}),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nick', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('nick',)
    ordering = ('nick',)
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Order)
class OrderCapacitor(admin.ModelAdmin):
    pass

@admin.register(Order_Capacitor)
class Order_CapacitorAdmin(admin.ModelAdmin):
    pass

@admin.register(Order_Resistor)
class Order_ResistorAdmin(admin.ModelAdmin):
    pass

@admin.register(Order_Chip)
class Order_ChipAdmin(admin.ModelAdmin):
    pass

