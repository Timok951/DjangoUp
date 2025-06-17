from .serializers import *
from rest_framework import viewsets, mixins
from main.models import *
from .premission import *


class CapacitorViewSet(viewsets.ModelViewSet):
    serializer_class = CapacitorSerializer 
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset=Capacitor.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset
    
class ProducerViewSet(viewsets.ModelViewSet):
    queryset=Capacitor.objects.all()
    serializer_class = ProducerSerializer 
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = Product_type.objects.all()
    serializer_class = Product_typeSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage

class ResistorViewSet(viewsets.ModelViewSet):
    queryset = Resistor.objects.all()
    serializer_class = ResistorSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class ChipViewSet(viewsets.ModelViewSet):
    queryset = Chip.objects.all()
    serializer_class = ChipSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class OrderViewSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class OrderCapacitorViewSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Order_Capacitor.objects.all()
    serializer_class = OrderCapacitorSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class OrderResistorViewSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Order_Resistor.objects.all()
    serializer_class = OrderResistorSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage


class OrderChipViewSet(mixins.ListModelMixin, 
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Order_Chip.objects.all()
    serializer_class = OrderChipSerializer
    permission_classes = [CustomPermissions]
    pagination_class = PaginationPage