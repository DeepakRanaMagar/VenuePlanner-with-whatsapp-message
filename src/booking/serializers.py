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
            # print("Booking Request Sent!")
            return booking_request
        except Exception as e:
            raise serializers.ValidationError("Booking Request Failed!",{e})
        


class BookInfoSerializer(serializers.ModelSerializer):
    '''
        serializes in the prespective of Customer
    '''
    venue = VenueSerializer(read_only=True)

    class Meta:
        model = BookingInfo
        fields = ['id', 'venue', 'date', 'status', 'request_sent_date', 'request_accepted_date']



class BookInfoDetailSerializer(serializers.ModelSerializer):
    '''
        Handle serialization to display customer's booking
    '''
    book_details = BookInfoSerializer(many=True, read_only=True, source='booking_details')

    class Meta:
        model = Customer
        fields = ['id','full_name','book_details']


class BookReqSerializer(serializers.ModelSerializer):
    '''
        Serializes on the prespective of Venue
    '''
    customer = CustomerSerializer(read_only = True)

    class Meta:
        model = BookingInfo
        fields = ['id', 'customer', 'date', 'status', 'request_sent_date', 'request_accepted_date']

class BookReqInfoDetailSerializer(serializers.ModelSerializer):
    req_details = BookReqSerializer(many = True, read_only = True, source = "request_details")

    class Meta:
        model = Venue
        fields = ['id', 'organization_name', 'req_details']