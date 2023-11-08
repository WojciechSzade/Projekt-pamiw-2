from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'color', 'model', 'price', 'type', 'year']