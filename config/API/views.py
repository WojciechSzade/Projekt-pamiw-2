from rest_framework.response import Response
from .models import Car, Brand
from .serializers import CarSerializer, BrandSerializer
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    def list(self, request, *args, **kwargs):
        if 'page' not in request.query_params:
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request, *args, **kwargs)