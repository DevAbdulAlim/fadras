from django.db import models

# Create your models here.
class Category(models.Model):
    name_en = models.CharField(max_length=255, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=255, verbose_name='Name (Arabic)')
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    image = models.ImageField(upload_to='images/categories')

    def __str__(self):
        return self.name_en


class Product(models.Model):
    name_en = models.CharField(max_length=200, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=200, verbose_name='Name (Arabic)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.name_en
    
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=255, verbose_name='Name (Arabic)')
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    original_image = models.ImageField(upload_to='images/product-variant-original')
    diagram_image = models.ImageField(upload_to='images/product-variant-diagrams')


    def __str__(self):
        return self.name_en