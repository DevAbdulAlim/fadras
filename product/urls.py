from django.urls import path
from .views import CategoryListView, ProductListView, ProductFilterView, ProductDetailsView

urlpatterns = [
    path('categories', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>', ProductListView.as_view(), name='products'),
    path('categories/<int:category_id>/<int:sub_category_id>', ProductFilterView.as_view(), name='filter_product'),
    path('product/<int:product_id>', ProductDetailsView.as_view(), name='product'),
]