from django.contrib import admin
from django.urls import path, include
from myapp.views import *
from products.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #products
    path("products/", include("products.urls"), name="Products_update"),
    # person
    path("person/", include("my_app.urls")),
]