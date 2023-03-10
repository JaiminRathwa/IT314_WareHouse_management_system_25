from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.

class Farmer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(
        max_length=10,
        validators = [
            RegexValidator(
                regex='^\d{10,11}$',
                message='Phone number must be valid',
                code='invalid_phone_number'
            ),
        ]
    )
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{first_name} {phone_number}'


class Crop(models.Model):
    name = models.CharField(max_length=200)
    max_storage_temperature = models.IntegerField()
    min_storage_temperature = models.IntegerField()
    max_storage_time_in_days = models.IntegerField()