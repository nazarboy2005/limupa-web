from django.contrib import admin

from products.models import ProductCategoryModel, ProductTagModel, ProductSizeModel, ProductModel, ProductColorModel, \
    ProductManufacturerModel, ProductImagesModel


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "head_category":
            kwargs["queryset"] = ProductCategoryModel.objects.filter(is_main=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']


@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']


@admin.register(ProductManufacturerModel)
class ProductManufacturerModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['name_or_code', 'created_at']
    search_fields = ['name_or_code', 'created_at']
    list_filter = ['name_or_code', 'created_at']


class ProductImagesModelAdmin(admin.StackedInline):
    model = ProductImagesModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    search_fields = ['name', 'price', 'created_at']
    list_filter = ['name', 'price', 'created_at']
    inlines = [ProductImagesModelAdmin]

