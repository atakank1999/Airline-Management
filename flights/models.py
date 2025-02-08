import uuid
from django.db import models
from airplanes.models import Airplane

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.flight_number} from {self.departure} to {self.destination}"
