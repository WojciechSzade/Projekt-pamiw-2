from django.forms import ModelForm
from API.models import Car, Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'price', 'type', 'year']