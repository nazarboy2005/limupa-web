from django.shortcuts import render
from django.views.generic import TemplateView


class ProductsListView(TemplateView):
    template_name = 'products/products-list.html'