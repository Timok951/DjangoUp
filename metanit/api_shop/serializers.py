from main.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = [
            'name',
            'description'
        ]
class Product_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_type
        fields = [
            'name',
            'discount'
        ]

class CapacitorSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Capacitor
        fields = [
            'name',
            'description',
            'price', 
            'capacity',
            'photo',
            'crate_date',
            'is_exist',
            'category',
            'producer',
            'product_type'
        ]

class ResistorSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Resistor
        fields = [
            'name',
            'description',
            'price',
            'resist',
            'photo',
            'create_date',
            'is_exists',
            'category',
            'producer',
            'product_type'
        ]


class ChipSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    #для нормальной конвертации
    class Meta:
        model = Chip
        fields = [
            'name',
            'description',
            'price',
            'photo',
            'create_date',
            'is_exists',
            'category',
            'producer',
            'product_type'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nick', 'phone', 'email']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'create_date',
            'comment',
            'user',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish'
        ]


class OrderCapacitorSerializer(serializers.ModelSerializer):
    capacitor = CapacitorSerializer(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order_Capacitor
        fields = ['capacitor', 'amount', 'order']


class OrderResistorSerializer(serializers.ModelSerializer):
    resistor = ResistorSerializer(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order_Resistor
        fields = ['resistor', 'amount', 'order']


class OrderChipSerializer(serializers.ModelSerializer):
    chip = ChipSerializer(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order_Chip
        fields = ['chip', 'amount', 'order']

