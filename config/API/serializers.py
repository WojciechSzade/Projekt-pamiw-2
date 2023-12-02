from .models import Car, Brand
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'url', 'brand', 'brand_name', 'model', 'color', 'price', 'type', 'year']
        

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = 'name', 'description'