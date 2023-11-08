from django.db import models

class Car(models.Model):
    TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchback'),
        ('suv', 'SUV'),
        ('mpv', 'MPV'),
        ('pickup', 'Pickup'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('wagon', 'Wagon'),
        ('van', 'Van'),
        ('truck', 'Truck'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('crossover', 'Crossover'),
        ('luxury', 'Luxury'),
        ('sports', 'Sports'),
        ('muscle', 'Muscle'),
        ('supercar', 'Supercar'),
        ('exotic', 'Exotic'),
        ('other', 'Other'),
    ]
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='other')
    year = models.IntegerField()

    def __str__(self):
        return self.brand + ' ' + self.model