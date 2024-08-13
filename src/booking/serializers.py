from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from datetime import date

from accounts.models import Customer, Venue

from .models import BookingInfo


class BookingSerializer(serializers.ModelSerializer):
    '''
        Handles the Venue Booking by Customer
    '''
    customer = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all())
    venue = serializers.PrimaryKeyRelatedField(queryset = Venue.objects.all())
    date = serializers.DateField(required=False)
    status = serializers.CharField(default = 'PENDING')
    request_sent_date = serializers.DateTimeField(required = False)
    request_accepted_date = serializers.DateTimeField(required = False)

    class Meta:
        model = BookingInfo
        fields = "__all__"

    def validate_date(self, value):
        '''
            Validates if the date of the venue booking request if is in past
        '''
        today = date.today()
        
        if value < today:
            raise serializers.ValidationError({
                "Invalid DateField": "DateField cannot be selected of the past"
            })
        return value

    def create(self, validated_data):
        try:
            booking_request = BookingInfo.objects.create(
                **validated_data
            )
            print("Booking Request Sent!")
            return booking_request
        except Exception as e:
            raise serializers.ValidationError("Booking Request Failed!",{e})
        