from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Venue

from .serializers import VenueSerializer


class VenueView(APIView):
    '''
        Handles the browse by property type
    '''
    permission_classes = [AllowAny, ] 

    def post(self, request):
        '''
            Handles POST() for the filter or querying
        '''
        property_type = request.data.get('property_type')
        price = request.data.get('price')
        name = request.data.get('organization_name')
        date = request.data.get('date')
        seat_capacity = request.data.get('seat_capacity')

        filters = {} # empty dictionary for key value pair 
        if property_type:
            filters['property_type'] = property_type
        
        if price:
            filters['price'] = price
        
        if name:
            filters['organization_name'] = name

        if date:
            filters['date'] = date

        if seat_capacity:
            filters['seat_capacity'] = seat_capacity

        try:
            venues = Venue.objects.filter(
                **filters
                ).all()
        except Venue.DoesNotExist as e:
            return Response(
                f"error: {str(e)}",
                status=status.HTTP_404_NOT_FOUND)
        
        try:
        
            serializer = VenueSerializer(venues, many=True)
            response = {
                "Venues": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
        
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request):
        # print('Venue list all api')
        venue_list = Venue.objects.all()
        serializer = VenueSerializer(venue_list, many=True)
            
        response = {
            "Venues": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)



class VenueSeatCapacityView(APIView):
    '''
        Handles the browse by property type
    '''
    permission_classes = [AllowAny, ] 

    def get(self, request):
        '''
            Handles GET() for the filtering the venues in the ascending order 
            based on Seat capacity of the venue
        '''
        
        try:
            venues = Venue.objects.all().order_by('seat_capacity')

        except Venue.DoesNotExist as e:
            return Response(
                f"error: {str(e)}",
                status=status.HTTP_404_NOT_FOUND)
        
        try:
        
            serializer = VenueSerializer(venues, many=True)
            response = {
                "Venues": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
        
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    