from django.urls import path
from .views import *


urlpatterns = [
    path('create/store/', StoreCreateView.as_view(), name='store-create'),
    path('update/store/<int:pk>/', StoreUpdateView.as_view(), name='store-update'),
    path('delete/store/<int:pk>/', StoreDeleteView.as_view(), name='store-delete'),
    path('list/store/', StoreListView.as_view(), name='store-list'),
    path('create/product/', ProductCreateView.as_view(), name='product-create'),
    path('update/product/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('delete/product/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('list/product/', ProductListView.as_view(), name='product-list'),
    path('search/product/', ProductSearchView.as_view(), name='product-search'),
    path('create/category/', CategoryCreateView.as_view(), name='category-create'),
    path('update/category/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('delete/category/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('list/category/', CategoryListView.as_view(), name='category-list'),  
]