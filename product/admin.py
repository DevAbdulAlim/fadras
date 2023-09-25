from django.contrib import admin
from .models import Category, SubCategory, Product, ProductDetails

# Register your models here.

class CustomPropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'title',)

    def product_name(self, obj):
        return obj.product.name_en
    
    product_name.short_description = "Product"



admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductDetails, ProductDetailsAdmin)



