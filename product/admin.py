from django.contrib import admin
from .models import Category, SubCategory, Product, ProductDetails, CustomProperty

# Register your models here.

class CustomPropertyAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'custom_properties_display',)

    def product_name(self, obj):
        return obj.product.name_en

    def custom_properties_display(self, obj):
        return ", ".join([cp.name for cp in obj.custom_properties.all()])
    
    product_name.short_description = "Product"
    custom_properties_display.short_description = 'Custom Properties'


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductDetails, ProductDetailsAdmin)
admin.site.register(CustomProperty, CustomPropertyAdmin)


