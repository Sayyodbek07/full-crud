from django.urls import path
from products.views import *

urlpatterns = [
    path("list/", ProductsListCreateApiView.as_view(), name="products-list-create"),
    path("update/<int:pk>/", ProductsUpdateDestroyApiView.as_view(), name="products-update"),
    path("destroy/<int:pk>/", ProductsUpdateDestroyApiView.as_view(), name="products-destroy"),
]