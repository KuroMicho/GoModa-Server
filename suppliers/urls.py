"""supplierProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from suppliers import views
from suppliers.views.supplierView import supplier_list

urlpatterns = [
    path('supplier/list/', views.supplier_list),
    path('supplier/create/', views.supplier_create), 
    path('supplier/get/<int:pk>/', views.supplier_get),
    path('supplier/put/<int:pk>/', views.supplier_put),
    path('supplier/delete/<int:pk>/', views.supplier_delete) 
]

