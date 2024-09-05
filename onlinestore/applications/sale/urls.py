from django.urls import path, re_path, include
#
from . import views

app_name = 'sale_app'


urlpatterns = [
    path('add-car/<pk>/', views.AddCarShop.as_view(), name='add_car'),
    path('list-car', views.ListProductCarShop.as_view(), name='list_car'),
    path('decrease-product/<pk>/', views.DecreaseCountProduct.as_view(), name='decrease_product'),
    path('increase-product/<pk>/', views.IncreaseCountProduct.as_view(), name='increase_product'),
    path('delete-product/<pk>/', views.DeleteProdcutView.as_view(), name='delete_product'),
    path('buy/', views.BuyView.as_view(), name='buy'),
]