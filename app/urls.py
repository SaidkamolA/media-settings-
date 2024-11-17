from django.urls import path
from .views import *
urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
]
