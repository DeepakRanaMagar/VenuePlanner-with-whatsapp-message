from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Venue

from .serializers import VenueSerializer


class VenueView(APIView):

    def post(self, request):
        property_type = request.data['property_type']
        try:
            venues = Venue.objects.filter(property_type=property_type)
            print(f'{property_type} is present haaii!!!!')
        except Venue.DoesNotExist as e:
            return Response(e)
        
        serializer = VenueSerializer(venues, many=True)
        response = {
            "Venues": serializer.data
        }
        print(response)
        return Response(response)
    