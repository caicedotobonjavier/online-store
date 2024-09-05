from django.db import models
#
from django.db.models import Sum, FloatField, Count, F


class CarShopManager(models.Manager):

    def total(self, user):
        total_pagar = self.filter(
            user=user
        ).aggregate(
            total=Sum(F('product__sale_price') * F('count'),
                    output_field=FloatField()
                    )                    
                )
        if total_pagar['total']:
            return total_pagar['total']
        else:
            return 0