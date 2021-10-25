from django.urls import path
from purchases.views.purchaseCreateView import PurchaseCreateView
from purchases.views.purchasesRetrieveView import PurchasesRetrieveView
from purchases.views.purchasesRetrieveSupplierView import PurchasesRetrieveSupplierView

urlpatterns = [
    path('product/<int:product_id>/purchase/', PurchaseCreateView.as_view(), name='purchases_create_view'),
    path('product/<int:product_id>/purchases/', PurchasesRetrieveView.as_view(), name="purchases_all_product_view"),
    path('supplier/<int:supplier_id>/purchases/', PurchasesRetrieveSupplierView.as_view(), name="purchases_all_product_by_supplier_view"),
]