from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework import status

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)