from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from flights.serializers import FlightSerializer
from .models import Airplane
from .serializers import AirplaneSerializer

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=True, url_path='flights')
    def flights(self, request, pk=None):
        airplane = self.get_object()
        flights = airplane.flights.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
