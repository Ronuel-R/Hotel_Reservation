from rest_framework import serializers
from client_hotel_reservation.models.bookings_model import Booking

class CreateBookingSerializer(serializers.ModelSerializer):
    check_in = serializers.DateField(required = True)
    check_out = serializers.DateField(required = True)
    class Meta:
        model = Booking
        fields = ['rooms', 'booking_name', 'phone_num','no_of_guest', 'check_in', 'check_out','description']
        extra_kwargs = {
            'booking_name': {'required': False},
            'phone_num': {'required': False},
            'no_of_guest': {'required': False},
        }

    # def validate_rooms(self, value):
        
    #     if not value.is_available(self.initial_data['check_in'], self.initial_data['check_out']):
    #         raise serializers.ValidationError("Room is not available for the specified period.")
    #     return value