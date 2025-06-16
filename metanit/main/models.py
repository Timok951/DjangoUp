from django.db import models

MAX_LENGTH = 255

#Category наследуется от класса и models.Model. Он делает из класса полноценную модель базы данных.
class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    #name — это строковое поле (CharField), которое обязательно должно быть заполнено
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    #Поле description — это текстовое поле (TextField), которое может быть пустым (null=True) или не заполненным (blank=True). 
    #Метод __str__ возвращает значение поля name, что позволяет легко идентифицировать объекты этой модели при работе с ними.
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Категория'
        #verbose_name= задаёт название этого поля для человека, которое будет использоваться в административном интерфейсе Django.
        verbose_name_plural = 'Категории'
    #Внутренний класс Meta содержит метаданные о модели. Здесь задаются названия для модели в единственном числе

class Producer(models.Model):
    name= models.CharField(max_length=MAX_LENGTH, verbose_name="Производитель")
    description = models.TextField(null=True, blank=True, verbose_name="Описание производителя")
    
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'

class Product_type(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Тип продукта')
    discount = models.FloatField(null=True, blank=True, verbose_name='Скидка')
    
    def __str__(self):
        return self.name
    
    class Meta: 
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Тип продукта'

class Capacitor(models.Model):
    name=models.CharField(max_length=MAX_LENGTH, verbose_name='Конденсатор')
    description= models.TextField(null=True, blank=True, verbose_name='Описание')
    price= models.FloatField(verbose_name="Цена")
    capacity= models.PositiveBigIntegerField(default=480, verbose_name="Ёмкость")
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    #Поле photo -Это поле для загрузки изображений (ImageField). 
    # Изображения будут сохраняться в директории image/%Y/%m/%d, 
    # где %Y — год, %m — месяц, %d — день. Поле может быть пустым (null=True) или не заполненным (blank=True). 
    crate_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exist = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")
    #Поле category - Это внешний ключ (ForeignKey), который ссылается на модель Category. Если попытаться удалить категорию, связанную с одеждой, то удаление будет заблокировано (on_delete=models.PROTECT). Также можно использовать вариант CASCADE для каскадного удаления. 
    producer = models.ForeignKey('Producer',on_delete=models.CASCADE, verbose_name='Производитель')
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, verbose_name='Тип продукта')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей)"
    
    class Meta:
        verbose_name = 'Конденсатор'
        verbose_name_plural = "Конденсатор"

class Resistor(models.Model):
    name=models.CharField(max_length=MAX_LENGTH, verbose_name='Резистор')
    description=models.TextField(null=True, blank=True, verbose_name='Описание')
    price=models.FloatField(null=True, blank=True, verbose_name='Цена')
    resist=models.PositiveBigIntegerField(default=10, verbose_name="Сопротивление")
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name="Изображение")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    producer = models.ForeignKey('Producer',on_delete=models.CASCADE, verbose_name='Производитель')
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, verbose_name='Тип продукта')

    
    def __str__(self):
        return f"{self.name} - ({self.price} рублей)"
    
    class Meta:
        verbose_name = 'Резистор'
        verbose_name_plural = "Резистор"
    
class Chip(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Чип')
    description=models.TextField(null=True, blank=True, verbose_name='Описание')
    price=models.FloatField(null=True, blank=True, verbose_name='Цена')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавлния на сайт')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

        
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, verbose_name='Производитель')
    product_type = models.ForeignKey('Product_type', on_delete=models.CASCADE, verbose_name='Тип продукта')


def __str__(self):
        return f"{self.name} - ({self.price} рублей)"
    
class Meta:
    verbose_name = 'Чип'
    verbose_name_plural = 'Чип'

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

MAX_LENGTH = 255


#AbstractBaseUser — это абстрактная базовая модель, от которой ты наследуешься, чтобы не писать всю логику с нуля (например, поле password, методы set_password(), check_password() и др.).
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class CustomUserManager(BaseUserManager):
    def create_user(self, nick, password=None, **extra_fields):
        if not nick:
            raise ValueError('Пользователь должен иметь ник')
        user = self.model(nick=nick, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        try:
            permission = Permission.objects.get(codename='add_order')
            user.user_permissions.add(permission)

        except Permission.DoesNotExist:
            print("Разрешение 'add_order' не найдено")

        return user

    def create_superuser(self, nick, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nick, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    nick = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Ник пользователя',
        unique=True
    )
    phone = models.CharField(max_length=14, verbose_name='Телефон', blank=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'nick'  
    REQUIRED_FIELDS = ['email']  

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    #Константные переменные, типов доставки
    SHOP = "SH"
    COURIER = "CR"
    PICKUPPOINT = "PP"
    TYPE_DELIVERY = [
        (SHOP, 'Самовывоз'),
        (COURIER,'Курьер' ),
        (PICKUPPOINT, 'Пункт выдачи заказов'),
    ]
    comment = models.TextField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Коментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=MAX_LENGTH,blank=True, null=True,verbose_name='Адрес доставки')   
    delivery_type= models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Тип доставки' )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения заказа')

    def __str__(self):
        return f"Заказ{self.pk} - {self.user.nick} ({self.date_create})"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Order_Capacitor(models.Model):
    capacitor = models.OneToOneField('Capacitor', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0, verbose_name='Колличество')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='ID заказа')
    
    def __str__(self):
        return f"Заказ {self.order.id} - {self.capacitor.name} x{self.amount}"    
    class Meta:
        verbose_name = 'Конденсатор'
        verbose_name_plural = 'Конденсатор'

class Order_Resistor(models.Model):
    resistor = models.OneToOneField('Resistor', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0, verbose_name='Колличество')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='ID заказа')
    
    def __str__(self):
        return f"Заказ {self.order.id} - {self.resistor.name} x{self.amount}"
    
    class Meta:
        verbose_name = 'Резистор'
        verbose_name_plural = 'Резистор'


class Order_Chip(models.Model): 
    chip = models.OneToOneField('Chip', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveBigIntegerField(default=0, verbose_name='Колличество')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='ID заказа')
    
    def __str__(self):
        return f"Заказ {self.order.id} - {self.chip.name} x{self.amount}"
    
    class Meta:
        verbose_name = 'Чип'
        verbose_name_plural = 'Чип'

