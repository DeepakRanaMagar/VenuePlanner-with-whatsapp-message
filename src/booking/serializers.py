from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from datetime import date

from accounts.models import Customer, Venue
from accounts.serializers import VenueSerializer, CustomerSerializer

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
            return booking_request
        except Exception as e:
            raise serializers.ValidationError("Booking Request Failed!",{e})
        


class BookInfoSerializer(serializers.ModelSerializer):

    venue = VenueSerializer(read_only=True)

    class Meta:
        model = BookingInfo
        fields = ['venue', 'date', 'status', 'request_sent_date', 'request_accepted_date']



class CustomerDisplaySerializer(serializers.ModelSerializer):
    '''
        Handle serialization to display
    '''
    customer = CustomerSerializer(read_only=True)
    # booking_details = BookInfoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'customer']
        # fields = ['id', 'customer', 'booking_details']




'''
    Nested serializer for the customer booking details
'''

# class CustomerBookDetailSerializer(serializers.ModelSerializer):
#     '''
#         Handles Serialization for the booking info
#     '''
#     customer = CustomerSerializer(read_only=True)
#     booking_info = BookDisplaySerializer(read_only = True ,many = True)

#     class Meta:
#         model = BookingInfo
#         fields = ['customer', 'booking_info']