from django.shortcuts import render
from django.views import View
from .models import Product
from django.utils.translation import activate
from django.conf import settings
from django.db.models import F

# Create your views here.
class ProductListView(View):
    def get(self, request):
        # Get user's selected language
        user_language = request.session.get('django_language', settings.LANGUAGE_CODE)

        # Determine which columns to select based on language
        name_column = F('name_en')
        description_column = F('description_en')
        if user_language == 'ar':
           name_column = F('name_ar')
           description_column = F('description_ar')

        # Fetch products with appropriate columns based on language
        products = Product.objects.annotate(
            name=name_column,
            description = description_column
        ).values('name', 'description', 'price')
        # Set the selected language for this view
        activate(user_language)

        return render(request, 'product/products.html', {'products': products})
