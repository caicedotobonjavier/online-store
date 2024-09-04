from django.contrib import admin
#
from .models import Product, Provider, Marca
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'barcode',
        'name',
        'description',
        'purchase_price',
        'sale_price',
        'provider',
        'marca',
        'image',
        'stock',
        'num_sale',
    )


admin.site.register(Product, ProductAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'razon_social',
        'nit',
        'web_site',       
        'address',
        'phone',
    )


admin.site.register(Provider, ProviderAdmin)


class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Marca, MarcaAdmin)