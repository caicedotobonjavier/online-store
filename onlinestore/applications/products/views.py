from django.shortcuts import render
#
from django.views.generic import TemplateView
#
from .models import Product
# Create your views here.


class ProductsView(TemplateView):
    template_name = 'products/products.html'
    paginate_by = 16


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        producto = self.request.GET.get('producto', '')
        if producto:
            context["all_products"] = Product.objects.filter(name__icontains=producto)
        else:
            context["all_products"] = Product.objects.all()
        return context
