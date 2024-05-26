from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import ProductCategoryModel


class ProductsListView(TemplateView):
    template_name = 'products/products-list.html'

    def get_context_data(self, **kwargs):
        categories = ProductCategoryModel.objects.filter(is_main=True)
        context = {
            'categories' : categories
        }
        return context