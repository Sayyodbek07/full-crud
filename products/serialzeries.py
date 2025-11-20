from rest_framework import serializers
from .models import ProductsList

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsList
        fields = "__all__"