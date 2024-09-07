from django.contrib import admin
#
from .models import Sale, SaleDetail, CarShop
# Register your models here.


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date_sale',
        'amount',
        'count',
        'discount',
        'user',
    )

admin.site.register(Sale, SaleAdmin)


class SaleDetailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sale',
        'product',
        'count',
        'purchase_price',
        'sale_price',
        'discount',
    )


admin.site.register(SaleDetail, SaleDetailAdmin)


class CarShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'barcode',
        'product',
        'count',
    )


admin.site.register(CarShop, CarShopAdmin)