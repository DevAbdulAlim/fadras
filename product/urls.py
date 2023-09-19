from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailsView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<int:category_id>', ProductListView.as_view(), name='products'),
    path('product/<int:product_id>', ProductDetailsView.as_view(), name='product'),
]