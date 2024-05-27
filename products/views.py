from django.views.generic import ListView, TemplateView

from products.models import ProductCategoryModel, ProductModel, ProductTagModel


class ProductsListView(ListView):
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        products = ProductModel.objects.all().order_by('created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        if tag:
            products = products.filter(tags__in=tag)

        if cat:
            products = products.filter(categories__in=cat)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.filter(is_main=True)
        context['tags'] = ProductTagModel.objects.all()
        return context


class ProductsDetailsView(ListView):
    template_name = 'products/product-details.html'
    context_object_name = 'product'

    def get_queryset(self):
        product = ProductModel.objects.get(id=self.kwargs["pk"])
        return product
