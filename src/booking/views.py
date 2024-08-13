from .serializers import BookingSerializer, CustomerDisplaySerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from accounts.models import Venue, Customer
from .models import BookingInfo


class CustomerBookingView(APIView):
    '''
        Endpoint for the Booking the venue by the client
    '''
    # permission_classes = [IsAuthenticated, ]
    @permission_classes([IsAuthenticated])
    def post(self, request):
        '''
            Handles POST request to create Booking request
        '''
        user = request.user
        try:
            isCustomer = Customer.objects.get(
                user = user
            )
            # print("True:",isCustomer)
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
        serializer = CustomerDisplaySerializer(customer_bookings, many=True)
        # serializer = CustomerBookDetailSerializer(customer_bookings, many=True)
        # serializer = BookedVenueSerializer(customer_bookings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class VenueBookingView(APIView):
    '''
        Endpoint for Booking Request to accept/reject the 
    '''
    @permission_classes([IsAuthenticated])
    def get(self, request):
        '''
            Handles POST() for the venue to fetch the booking details requested by the customer
        '''
        user = request.user

        try:
            isVenue = Venue.objects.get(
                user=user
            )
            print("true venue: ", isVenue)
        except Venue.DoesNotExist as e:
            return Response({"error": "User is not a venue", "details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        venue_bookings = BookingInfo.objects.filter(
            venue = isVenue
        )
        serializer = BookDisplaySerializer(venue_bookings, many=True)
        # print(serializer.data) 
        
        return Response(serializer.data, status=status.HTTP_200_OK)
