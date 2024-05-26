from django.db import models


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=64)
    is_main = models.BooleanField()
    head_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub_categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
