from django.db import models
from django.utils.timezone import now
from django.core import serializers
import uuid
import json


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=20, default='undefined')
    # - Name
    description = models.TextField(null=True)
    # - Description

    def __str__(self):
        # - __str__ method to print a car make object
        return self.name + ": " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    # - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
    name = models.CharField(null=False, max_length=40, default='undefined')
    # - Name
    dealer_id = models.CharField(
        null=False, max_length=40, default='undefined')
    # - Dealer id, used to refer a dealer created in cloudant database
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    SPORTS = 'Sports'
    HATCHBACK = 'Hatchback'
    CONVERTIBLE = 'Convertible'
    MINIVAN = 'Minivan'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (SPORTS, 'Sports'),
        (HATCHBACK, 'Hatchback'),
        (CONVERTIBLE, 'Convertible'),
        (MINIVAN, 'Minivan'),
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=COUPE
    )
    # - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    year = models.DateField(null=False)
    # - Year (DateField)
    year = models.DateTimeField('date designed')

    def __str__(self):
        return self.type
    # - __str__ method to print a car make object

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
