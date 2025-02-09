from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['departure_time'] >= data['arrival_time']:
            raise serializers.ValidationError("Departure time must be before arrival time.")
        if data["departure"] == data["destination"]:
            raise serializers.ValidationError("Departure and destination must be different.")
        return data
    class Meta:
        model = Flight
        fields = '__all__'
