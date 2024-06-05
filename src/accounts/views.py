from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Venue
from .serializers import (CustomerRegistrationSerializer,
                          VenueRegistrationSerializer)


# Create your views here.
class VenueRegisterView(APIView):
    '''
        Handles the endpoint for the Venue Registration
    '''
    permission_classes = [AllowAny, ]

    def post(self, request):
        '''
            Handles the POST request for the Venue register endpoint
        '''
        # print(request.data)
        serializer = VenueRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "data": "Venue successfully registered"
                    }, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {
                        "error":str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class CustomerRegisterView(APIView):
    '''
        Handles the endpoint for the Venue Registration
    '''
    permission_classes = [AllowAny, ]

    def post(self, request):
        '''
            Handles the POST request for the Venue register endpoint
        '''
        print(request.data)
        serializer = CustomerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {
                        "data": "your account is successfully created."
                    }, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {
                        "error":str(e)
                    }, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
