from django.urls import path
from .views import CategoryListView, BrandListView, ProductListView


app_name = 'products'
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('brands/<int:pk>/', BrandListView.as_view(), name='brand-list'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product-list'),
]