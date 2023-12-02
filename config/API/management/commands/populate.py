from faker import Faker
from faker_vehicle import VehicleProvider
from API.models import Brand, Car

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--cars', type=int, help='Indicates the number of cars to be created')
    
    def handle(self, **options):
        cars_desired_population = options['cars'] or 100

        faker = Faker()
        faker.add_provider(VehicleProvider)

        car_count = Car.objects.all().count()

        colors = ["red", "green", "blue", "black", "white", "yellow", "orange", "darkblue", "gray", "silver", "darkgreen", "brown"]

        for i in range(cars_desired_population - car_count):
            car_data = faker.vehicle_object()
            brand = car_data['Make']
            try:
                brand = Brand.objects.get(name=brand)
            except:
                description = brand + ' is a car brand.'
                brand = Brand.objects.create(name=brand, description=description)
            car_data['Category'] = car_data['Category'].lower()
            if car_data['Category'] not in [choice[0] for choice in Car.TYPE_CHOICES]:
                car_data['Category'] = 'other'
            car = Car.objects.create(
                brand=brand,
                model=car_data['Model'],
                color=colors[faker.random_int(0, len(colors) - 1)],
                price=faker.random_int(1000, 1000000, step=100),
                type=car_data['Category'],
                year=car_data['Year']
            )
            print("created " + str(car))
            
        car_count = Car.objects.all().count()
            
        for i in range(-(cars_desired_population - car_count)):
            deleted_car = Car.objects.get(id=faker.random_int(1, car_count))
            deleted_car.delete()
            print("deleted " + str(deleted_car))
        
        car_count = Car.objects.all().count()
        print("cars population: " + str(car_count))
            
            
    