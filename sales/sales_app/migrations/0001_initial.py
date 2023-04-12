# Generated by Django 4.0.3 on 2023-04-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('size', models.DecimalField(decimal_places=1, max_digits=3)),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('sku', models.CharField(max_length=50)),
            ],
        ),
    ]
