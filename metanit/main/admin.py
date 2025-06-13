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

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

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