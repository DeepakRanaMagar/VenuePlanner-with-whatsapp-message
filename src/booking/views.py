from django.shortcuts import render

from .serializers import BookingSerailizer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import Venue, Customer
from .models import BookingInfo

class BookingView(APIView):
    '''
        Endpoint for the Booking the venue by the client
    '''
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        print('booking endpoint')
        return Response('Check terminal')
