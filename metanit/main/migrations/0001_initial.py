# Generated by Django 5.2.2 on 2025-06-11 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Производитель')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание производителя')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производитель',
            },
        ),
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тип продукта')),
                ('discount', models.FloatField(blank=True, null=True, verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Тип продукта',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=255, verbose_name='Ник пользователя')),
                ('phone', models.CharField(blank=True, max_length=14, verbose_name='Телефон')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
                ('password', models.TextField(max_length=255, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователь',
            },
        ),
        migrations.CreateModel(
            name='Capacitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Конденсатор')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('capacity', models.PositiveBigIntegerField(default=480, verbose_name='Ёмкость')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение')),
                ('crate_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')),
                ('is_exist', models.BooleanField(default=True, verbose_name='Доступность к заказу')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producer', verbose_name='Производитель')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_type', verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name': 'Конденсатор',
                'verbose_name_plural': 'Конденсатор',
            },
        ),
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Чип')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавлния на сайт')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Доступность к заказу')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producer', verbose_name='Производитель')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_type', verbose_name='Тип продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Capacitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0, verbose_name='Колличество')),
                ('capacitor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.capacitor')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='ID заказа')),
            ],
            options={
                'verbose_name': 'Конденсатор',
                'verbose_name_plural': 'Конденсатор',
            },
        ),
        migrations.CreateModel(
            name='Order_Chip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0, verbose_name='Колличество')),
                ('chip', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.chip')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='ID заказа')),
            ],
            options={
                'verbose_name': 'Чип',
                'verbose_name_plural': 'Чип',
            },
        ),
        migrations.CreateModel(
            name='Resistor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Резистор')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('resist', models.PositiveBigIntegerField(default=10, verbose_name='Сопротивление')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Доступность к заказу')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producer', verbose_name='Производитель')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product_type', verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name': 'Резистор',
                'verbose_name_plural': 'Резистор',
            },
        ),
        migrations.CreateModel(
            name='Order_Resistor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveBigIntegerField(default=0, verbose_name='Колличество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='ID заказа')),
                ('resistor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.resistor')),
            ],
            options={
                'verbose_name': 'Резистор',
                'verbose_name_plural': 'Резистор',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user', verbose_name='Пользователь'),
        ),
    ]
