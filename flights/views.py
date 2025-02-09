from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from reservations.serializers import ReservationSerializer
from .models import Flight
from .serializers import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer

    def get_queryset(self):
        queryset = Flight.objects.all()

        departure = self.request.query_params.get('departure')
        destination = self.request.query_params.get('destination')
        departure_time = self.request.query_params.get('departure_time')
        arrival_time = self.request.query_params.get('arrival_time')

        if departure:
            queryset = queryset.filter(departure__icontains=departure)
        if destination:
            queryset = queryset.filter(destination__icontains=destination)
        if departure_time:
            queryset = queryset.filter(departure_time__icontains=departure_time)
        if arrival_time:
            queryset = queryset.filter(arrival_time__icontains=arrival_time)

        return queryset



    @action(detail=True, url_path='reservations')
    def reservations(self, request, pk=None):
        flight = self.get_object()
        reservations = flight.reservation_set.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
