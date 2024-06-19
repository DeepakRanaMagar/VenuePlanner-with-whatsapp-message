from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
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

        filters = {} # empty dictionary for key value pair 
        if property_type:
            filters['property_type'] = property_type
        
        if price:
            filters['price'] = price
        
        if name:
            filters['organization_name'] = name

        if date:
            filters['date'] = date

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
    

class VenueSeatCapacityView(APIView):
    '''
        Handles the browse by property type
    '''
    permission_classes = [AllowAny, ] 

    def get(self, request):
        '''
            Handles GET() for the filter or querying
        '''
        
        try:
            venues = Venue.objects.order_by('price')
            print(venues)
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
    