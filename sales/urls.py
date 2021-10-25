from django.urls import path
from sales.views.saleCreateView import SaleCreateView
from sales.views.salesRetrieveView import SalesRetrieveView

urlpatterns = [
    path('product/<int:product_id>/sale/', SaleCreateView.as_view(), name="sale_create_view"),
    path('product/<int:product_id>/sales/', SalesRetrieveView.as_view(), name="sales_all_product_view")
]