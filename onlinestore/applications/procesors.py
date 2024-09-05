from applications.sale.models import CarShop


def count_products(request):
    if request.user.is_authenticated:
        cantidad = CarShop.objects.filter(user=request.user).count()
        return {
            'count_products': cantidad
        }
    else:
        return {
            'count_products': 0
        }