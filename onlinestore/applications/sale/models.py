from django.db import models
#
from model_utils.models import TimeStampedModel
#
from django.conf import settings
#
from applications.products.models import Product
#
from .managers import CarShopManager
# Create your models here.


class Sale(TimeStampedModel):
    date_sale = models.DateField('Fecha de Fecha')
    amount = models.DecimalField('Monto de la compra', max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField('Cantidad de productos')
    discount = models.DecimalField('Descuento', max_digits=4, decimal_places=2, default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sale_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    
    def __str__(self):
        return '[ID Venta: ' + str(self.id) + ' - ' + str(self.date_sale) + ']'



class SaleDetail(TimeStampedModel):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.DecimalField('Descuento Producto', max_digits=3, decimal_places=2, default=0)
    count = models.PositiveIntegerField('Cantidad')
    purchase_price = models.DecimalField('Precio Compra', max_digits=5, decimal_places=2)
    sale_price = models.DecimalField('Precio Venta', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
    
    def __str__(self):
        return str(self.id)



class CarShop(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carshop_user')
    barcode = models.CharField('Codigo Barras', max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField('Cantidad')

    objects = CarShopManager()

    class Meta:
        verbose_name = 'Carrito de Compras'
        verbose_name_plural = 'Carritos de Compras'
    
    def __str__(self):
        return self.product.name


