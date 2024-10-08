from datetime import date

from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from accounts.models import Customer, Venue
from accounts.serializers import CustomerSerializer, VenueSerializer

from .message import sendWhatsappMessage
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
            customer_phone_num = booking_request.customer.phone_num
            # print('Customer_phone_num:', customer_phone_num)
            venue_phone_num = booking_request.venue.phone_num

            # Load the message templates
            customer_message = render_to_string('messages/customer_request_sent.txt', {
                'customer_name': booking_request.customer.user.username,
                'venue_name': booking_request.venue.organization_name,
                'booking_date': booking_request.date,
            })


            venue_message = render_to_string('messages/venue_notification.txt', {
                'venue_name': booking_request.venue.organization_name,
                'customer_name': booking_request.customer.user.username,
                'booking_date': booking_request.date,
            })      
            
            # Call the sendWhatsappMessage function
            if booking_request:
                sendWhatsappMessage(customer_phone_num, customer_message)
                sendWhatsappMessage(venue_phone_num, venue_message)

            
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
        fields = ['id', 'venue', 'date', 'status', 'request_sent_date', 'request_accepted_date', 'request_rejected_date']



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
        fields = ['id', 'customer', 'date', 'status', 'request_sent_date', 'request_accepted_date', 'request_rejected_date']

class BookReqInfoDetailSerializer(serializers.ModelSerializer):
    req_details = BookReqSerializer(many = True, read_only = True, source = "request_details")

    class Meta:
        model = Venue
        fields = ['id', 'organization_name', 'req_details']

class BookReqUpdateSerializer(serializers.ModelSerializer):
    '''
        handles the serialization for the accepting/rejecting the Incoming booking request
    '''
    class Meta:
        model = BookingInfo
        fields = ['status', 'request_accepted_date', 'request_rejected_date']
    
    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)

        if status == 'ACCEPTED':
            instance.request_accepted_date = timezone.now()

        if status == "DECLINED":
            instance.request_rejected_date = timezone.now()
        
        instance.status = status
        instance.save()



        booking_request = instance
        customer_phone_num = booking_request.customer.phone_num
        venue_phone_num = booking_request.venue.phone_num

        # Load the message templates
        customer_message = render_to_string('messages/customer_request_accepted.txt', {
            'customer_name': booking_request.customer.user.username,
            'venue_name': booking_request.venue.organization_name,
            'booking_date': booking_request.date,
        })

        venue_message = render_to_string('messages/venue_request_accepted.txt', {
            'venue_name': booking_request.venue.organization_name,
            'customer_name': booking_request.customer.user.username,
            'booking_date': booking_request.date,
        })      
            
            # Call the sendWhatsappMessage function
        try:
            sendWhatsappMessage(customer_phone_num, customer_message)
            sendWhatsappMessage(venue_phone_num, venue_message)
                
        except Exception as e:
            print("Error sending whatsapp message",{e})
            return serializers.ErrorDetail(e)
        
        return instance