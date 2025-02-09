from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework import status

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def create(self, request, *args, **kwargs):
        flight = self.get_object().flight
        if flight.reservation_set.count() >= flight.airplane.capacity:
            return Response({"message": "Flight is full"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)