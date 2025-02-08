from django.db import models
import uuid
from flights.models import Flight

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            self.reservation_code = uuid.uuid4().hex[:6].upper()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"Reservation {self.reservation_code} for {self.passenger_name}"
