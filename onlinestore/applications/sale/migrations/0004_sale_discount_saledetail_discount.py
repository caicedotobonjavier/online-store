# Generated by Django 5.1 on 2024-09-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_alter_carshop_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Descuento'),
        ),
        migrations.AddField(
            model_name='saledetail',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Descuento Producto'),
        ),
    ]
