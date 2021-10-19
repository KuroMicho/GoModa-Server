from django.urls import path
from suppliers.views.supplierCreateView import SupplierCreateView
from suppliers.views.suppliersRetrieveView import SuppliersRetrieveView
from suppliers.views.supplierRUDView import SupplierRUDView

urlpatterns = [
    path('supplier/', SupplierCreateView.as_view(), name="supplier_create_view"),
    path('suppliers/', SuppliersRetrieveView.as_view(), name="supplier_all_view"),
    path('supplier/<int:id>/', SupplierRUDView.as_view(), name="supplier_rud_view"),
]