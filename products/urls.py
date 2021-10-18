from django.urls import path
from products.views.productCreateView import ProductCreateView
from products.views.productsRetrieveView import ProductsRetrieveView
from products.views.productRUDView import ProductRUDView
from products.views.productsRetrieveOnhandView import ProductsRetrieveOnhandView

urlpatterns = [
    path('product/', ProductCreateView.as_view(), name="product_create_view"),
    path('products/', ProductsRetrieveView.as_view(), name="products_all_view"),
    path('products-filter/', ProductsRetrieveOnhandView.as_view(), name="products_all_filter_view"),
    path('product/<int:id>/', ProductRUDView.as_view(), name="product_rud_view"),
]
