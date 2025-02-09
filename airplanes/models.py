from django.db import models


class Airplane(models.Model):
    tail_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} - {self.tail_number}"
