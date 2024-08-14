from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Customer, Venue

from .models import BookingInfo
from .serializers import (BookInfoDetailSerializer, BookingSerializer,
                          BookReqInfoDetailSerializer, BookReqUpdateSerializer)


class CustomerBookingView(APIView):
    '''
        Endpoint for the Booking the venue by the client
    '''
    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        '''
            Handles POST request to create Booking request
        '''
        user = request.user
        try:
            isCustomer = Customer.objects.get(
                user = user
            )
        except Exception as e:
            return('Customers can only send book request.', {e})
        
        data = request.data

        if isCustomer:
            data['customer'] = isCustomer.id
            serializer = BookingSerializer(data=data)
            
            if serializer.is_valid():
            
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            
                except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        '''
            Handles the GET request, that will fetch all the bookings made to the venue 
        '''
        user = request.user
        try:
            isCustomer = Customer.objects.get(
                user = user
            )
            
        except Customer.DoesNotExist as e:
            return Response("Only Customer allowed to view the booking.", status=status.HTTP_400_BAD_REQUEST)
        
        customer_bookings = BookingInfo.objects.filter(
            customer = isCustomer
        )
        serializer = BookInfoDetailSerializer(isCustomer)
        return Response(serializer.data, status=status.HTTP_200_OK)



class VenueBookingView(APIView):
    '''
        Endpoint for Booking Request to accept/reject the 
    '''
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        '''
            Handles POST() for the venue to fetch the booking details requested by the customer
        '''
        user = request.user

        try:
            isVenue = Venue.objects.get(
                user=user
            )
        except Venue.DoesNotExist as e:
            return Response({"error": "User is not a venue", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        venue_bookings = BookingInfo.objects.filter(
            venue = isVenue
        )
        serializer = BookReqInfoDetailSerializer(isVenue)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        '''
            Handle the POST(), enables the venue to accept or reject the incoming booking request
        '''
        user = request.user
        try:
            isVenue = Venue.objects.get(
                user=user
            )
        except Venue.DoesNotExist as e:
            return Response({"error": "User is not a venue", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        booking_id = request.data.get('booking_id')

        new_status = request.data.get('status')
        if new_status not in ['ACCEPTED', 'DECLINED']:
            return Response({"error": "Invalid status. Status must be 'ACCEPTED' or 'DECLINED'."}, status=status.HTTP_400_BAD_REQUEST)
    
        try:
            venue_bookings = BookingInfo.objects.get(id=booking_id, venue = isVenue)
        except BookingInfo.DoesNotExist:
            return Response({"error": "Booking request not found or you are not authorized to update this booking."}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        serializer = BookReqUpdateSerializer(venue_bookings, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)