from django.shortcuts import render
#
from applications.products.models import Product
#
from .models import CarShop
#
from django.views.generic import View, ListView
#
from django.http import HttpResponseRedirect
#
from django.urls import reverse_lazy, reverse
#
from .functions import make_purchase
#
import datetime
# Create your views here.


class AddCarShop(View):
    
    def post(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        product = Product.objects.get(id=dato)
        cod = product.barcode
        usuario = self.request.user

        producto, created = CarShop.objects.get_or_create(
            barcode = cod,
            user = usuario,
            defaults={          
                'product' : product,
                'count' : 1
            }            
        )

        print('creado' + str(created))
        print('obtenido' + str(producto))

        if not created:
            producto.count += 1
            producto.save()
        

        return HttpResponseRedirect(
            reverse(
                'products_app:products'
            )
        )



class ListProductCarShop(ListView):
    template_name = 'sale/list-carshop.html'
    context_object_name = 'products'

    def queryset(self):
        return CarShop.objects.filter(user=self.request.user).order_by('product__name')


    def get_context_data(self, **kwargs):
        context = super(ListProductCarShop, self).get_context_data(**kwargs)
        context['total'] = CarShop.objects.total(self.request.user)
        return context
    


class DecreaseCountProduct(View):
    
    def get(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        producto = CarShop.objects.get(id=dato)
        if producto.count > 1:
            producto.count -= 1
            producto.save()
        else:
            producto.delete()
        

        return HttpResponseRedirect(
            reverse(
                'sale_app:list_car'
            )
        )
        


class IncreaseCountProduct(View):
    
    def get(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        producto = CarShop.objects.get(id=dato)
        producto.count += 1
        producto.save()

        return HttpResponseRedirect(
            reverse(
                'sale_app:list_car'
            )
        ) 



class DeleteProdcutView(View):

    def get(self, request, *args, **kwargs):
        dato = self.kwargs['pk']
        producto = CarShop.objects.get(id=dato).delete()
        print('Producto eliminado', str(producto))

        return HttpResponseRedirect(
            reverse(
                'sale_app:list_car'
            )
        )


class BuyView(View):

    def get(self, request, *args, **kwargs):

        make_purchase(
            self,
            date_sale = datetime.datetime.now(),
            amount = 0,
            count = 0, 
            user = self.request.user
        )
        
        return HttpResponseRedirect(
            reverse(
                'home_app:index'
            )
        )