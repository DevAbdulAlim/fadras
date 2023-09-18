from django.urls import path
from .views import ProductListView, ProductDetailsView

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('<int:product_id>/', ProductDetailsView.as_view(), name='product'),
]