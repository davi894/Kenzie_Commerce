# Generated by Django 4.0.7 on 2023-03-09 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('address', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_order', to='products.product'),
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='address.address'),
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(related_name='products_cart', through='orders.OrdersProducts', to='products.product'),
        ),
    ]
