from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from accounts.models import Customer, Venue

from .models import BookingInfo


class BookingSerailizer(serializers.ModelSerializer):
    '''
        Handles the Venue Booking by Customer
    '''
    venue = serializers.PrimaryKeyRelatedField(queryset = Venue.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all())
    date = serializers.DateField(required = True)
    status = serializers.CharField(default = 'pending')
    request_sent_date = serializers.DateTimeField(required = True)
    request_accepted_date = serializers.DateTimeField(required = False)

    class Meta:
        model = BookingInfo
        fields = "__all__"

    
    def create(self, validated_data):
        try:
            booking_request = BookingInfo.objects.create(
                **validated_data
            )
            print("Booking Request Sent!")
            return booking_request
        except Exception as e:
            raise serializers.ValidationError("Booking Request Failed!",{e})
        