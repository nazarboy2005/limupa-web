from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=64)
    is_main = models.BooleanField()
    head_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='sub_categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProductColorModel(models.Model):
    name_or_code = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name_or_code

    def __str__(self):
        return self.name_or_code

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class ProductManufacturerModel(models.Model):
    name = models.CharField(max_length=16)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'


class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product-images', null=True)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    count = models.PositiveSmallIntegerField()

    manufacturer = models.ForeignKey(ProductManufacturerModel, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(ProductSizeModel, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    categories = models.ManyToManyField(ProductCategoryModel, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_discounted(self):
        return self.discount != 0

    def discounted_price(self):
        return self.price * (100 - self.discount) / 100

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductImagesModel(models.Model):
    image = models.ImageField(upload_to='product-detail-images')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    def __repr__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'