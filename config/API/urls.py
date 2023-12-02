from django.urls import include, path
from rest_framework import routers
from .views import CarViewSet, BrandViewSet 

router = routers.DefaultRouter()
router.register(r'car', CarViewSet, basename="car")
router.register(r'brand', BrandViewSet, basename="brand")

urlpatterns = [
    path('', include(router.urls)),
]