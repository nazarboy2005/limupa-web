from django.contrib import admin
from products.models import ProductCategoryModel

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['name', 'created_at']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "head_category":
            kwargs["queryset"] = ProductCategoryModel.objects.filter(is_main=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)