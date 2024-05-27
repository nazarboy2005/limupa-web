from django.urls import path
from products.views import ProductsListView, ProductsDetailsView


app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='list'),
    path('details/<int:pk>/', ProductsDetailsView.as_view(), name='details')
]