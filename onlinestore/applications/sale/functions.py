from .models import Sale, SaleDetail, CarShop
#
from applications.products.models import Product

def make_purchase(self, **dates):
    cantidad = CarShop.objects.filter(user=dates['user']).count()
    if cantidad > 0:
        productos = CarShop.objects.filter(user=dates['user'])
        
        venta = Sale.objects.create(
            date_sale = dates['date_sale'],
            amount = dates['amount'],
            count = dates['count'],
            user = dates['user']
        )

        monto = 0
        cantidad = 0

        lista_productos = []
        productos_vendidos = []

        for producto in productos:
            detalle = SaleDetail(
                sale = venta,
                product = producto.product,
                count = producto.count,
                purchase_price = producto.product.purchase_price,
                sale_price = producto.product.sale_price
            )
            lista_productos.append(detalle)

            #
            vendidos = producto.product
            vendidos.stock -= producto.count
            vendidos.num_sale += producto.count
            #
            productos_vendidos.append(vendidos)

            monto += producto.product.sale_price * producto.count
            cantidad += producto.count
        
        SaleDetail.objects.bulk_create(
            lista_productos
        )

        Product.objects.bulk_update(
            productos_vendidos,
            ['stock', 'num_sale']
        )

        venta.amount = monto
        venta.count = cantidad
        venta.save()        

        CarShop.objects.filter(user=dates['user']).delete()


    else:
        print('No hay productos en el carrito')