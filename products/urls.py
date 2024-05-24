from django.urls import path
from products.views import ProductsListView


app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list')
]