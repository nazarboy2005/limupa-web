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


class ProductsDetailsView(TemplateView):
    template_name = 'products/product-details.html'
    model = ProductModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = ProductModel.objects.get(id=kwargs["pk"])
        product_categories = product.categories.all()
        same_cat_products = ProductModel.objects.filter(categories__in=product_categories).exclude(
            id=product.id).distinct()

        context.update({
            'product': product,
            'same_cat_products': same_cat_products[:15],
        })

        return context
