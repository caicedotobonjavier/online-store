# Generated by Django 5.1 on 2024-09-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_alter_carshop_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carshop',
            name='barcode',
            field=models.CharField(max_length=10, verbose_name='Codigo Barras'),
        ),
    ]
