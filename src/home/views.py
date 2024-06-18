from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Venue

from .serializers import VenueSerializer


class VenueView(APIView):

    def post(self, request):
        property_type = request.data
        # print(property_type)
        try:
            venues = Venue.objects.filter(property_type=property_type).all()
        except Venue.DoesNotExist as e:
            return Response(e)
        
        serializer = VenueSerializer(venues, many=True)
        print(serializer)
        response = {
            "Venues": serializer.data
        }
        print(response)
        return Response(response)
        # return Response(property_type)
    