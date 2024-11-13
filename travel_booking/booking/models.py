from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateField()
    seats = models.IntegerField()

def _str_(self):
    return f"{self.name}"