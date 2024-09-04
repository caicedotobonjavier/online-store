from django.urls import path, re_path, include
#
from . import views

app_name = 'products_app'


urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products'),
]