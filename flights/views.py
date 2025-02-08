from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from reservations.serializers import ReservationSerializer
from .models import Flight
from .serializers import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    @action(detail=True, url_path='reservations')
    def reservations(self, request, pk=None):
        flight = self.get_object()
        reservations = flight.reservations.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
