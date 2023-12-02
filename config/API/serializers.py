from .models import Car, Brand
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    brand_url = serializers.HyperlinkedRelatedField(source='brand', view_name='brand-detail', read_only=True)
    class Meta:
        model = Car
        fields = ['id', 'url', 'brand', 'brand_url', 'model', 'color', 'price', 'type', 'year']
        

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'