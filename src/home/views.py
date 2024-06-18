from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Venue

from .serializers import VenueSerializer


class VenueView(APIView):

    def get(self, request):
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        response = {
            "Venues": serializer.data
        }
        return Response(response)