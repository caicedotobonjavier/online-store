from django.db import models
#
from model_utils.models import TimeStampedModel
# Create your models here.


class Provider(TimeStampedModel):
    razon_social = models.CharField('Nombre Provedor', max_length=100, unique=True)
    nit = models.CharField('Numero Identificacion', max_length=50, unique=True)
    web_site = models.URLField('Pagina Web', max_length=200, null=True, blank=True)
    address = models.CharField('Direccion', max_length=50, null=True, blank=True)
    phone = models.CharField('Telefono', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    

    def __str__(self):
        return self.razon_social
    


class Marca(TimeStampedModel):
    name = models.CharField('Nombre Marca', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    barcode = models.CharField('Codigo Barras', max_length=10, unique=True)
    name = models.CharField('Nombre', max_length=50)
    description = models.TextField('Descripcion', null=True, blank=True)
    purchase_price = models.DecimalField('Precio Compra', max_digits=5, decimal_places=2)
    sale_price = models.DecimalField('Precio Venta', max_digits=5, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to='products', null=True, blank=True)
    stock = models.IntegerField('Stock', default=0)
    num_sale = models.PositiveIntegerField('Veces Vendido', default=0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name