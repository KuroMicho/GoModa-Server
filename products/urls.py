from django.urls import path
from products.views.productCreateView import ProductCreateView

urlpatterns = [
    path('product/', ProductCreateView.as_view(), name="product_create_view")
]