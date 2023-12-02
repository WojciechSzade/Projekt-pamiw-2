from django.urls import include, path
from .views import *

app_name = "webapp"

urlpatterns = [
    path('', index, name='index'),
    path('cars_list/', cars_list, name='cars_list'),
    path('cars_list/page=<int:page>', cars_list, name='cars_list'),
    path('car_details/<int:id>', car_details, name='car_details'),
    path('car_create/', car_create, name='car_create'),
    path('car_update/<int:id>', car_update, name='car_update'),
    path('car_delete/<int:id>', car_delete, name='car_delete'),
    path('brands_list/', brands_list, name='brands_list'),
    path('brands_list/page=<int:page>', brands_list, name='brands_list'),
    path('brand_details/<str:name>', brand_details, name='brand_details'),
    path('brand_create/', brand_create, name='brand_create'),
    path('brand_update/<str:name>', brand_update, name='brand_update'),
    path('brand_delete/<str:name>', brand_delete, name='brand_delete'),
]