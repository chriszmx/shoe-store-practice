# Generated by Django 4.0.3 on 2023-04-11 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0003_shoppingcart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='shoe_inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='sales_app.shoeinventory'),
        ),
    ]