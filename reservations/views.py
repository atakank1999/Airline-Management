from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def perform_create(self, serializer):
        reservation = serializer.save()
        flight = reservation.flight
        subject = f"Reservation for flight {flight.flight_number}"
        message = f"Dear {reservation.passenger_name},
        \n\nYou have successfully booked a flight from {flight.departure} to {flight.destination}.
        \n\nThank you for choosing our airline.
        \n\n Reservation Code: {reservation.reservation_code},"

        recipient_email = reservation.passenger_email
        send_mail(
            subject, 
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False
        )
        
    def create(self, request, *args, **kwargs):
        flight = self.get_object().flight
        if flight.reservation_set.count() >= flight.airplane.capacity:
            return Response({"message": "Flight is full"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)