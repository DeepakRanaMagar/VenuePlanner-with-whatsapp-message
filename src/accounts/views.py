from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Venue
from .serializers import (CustomerRegistrationSerializer,
                          UpdateProfileSerializer, VenueRegistrationSerializer)


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



class VenueLoginView(APIView):
    '''
        Handles the endpoint for logging in the venue
    '''

    permission_classes = [AllowAny, ]

    def post(self, request):
        '''
            Handles POST request for username and password to retrieve auth token
        '''

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "user_id": user.id
                }, status= status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "Login Failed. Invalid Credentials"
                }, status=status.HTTP_401_UNAUTHORIZED
            )
        


class CustomerLoginView(APIView):
    '''
        Handles the endpoint for logging in the venue
    '''

    permission_classes = [AllowAny, ]

    def post(self, request):
        '''
            Handles POST request for username and password to retrieve auth token
        '''

        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "user_id": user.id
                }, status= status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "Login Failed. Invalid Credentials"
                }, status=status.HTTP_401_UNAUTHORIZED
            )
        


class UpdateProfileView(APIView):
    '''
        Handles the endpoint for Update profile.
    '''
    permission_classes = [IsAuthenticated, ]

    def put(self, request):
        '''
            Handles the Update() request for the EditProfile fields
        '''
        print(request.user.username)
        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save()
                return Response(
                    {
                        f"Your profile is successfully updated"
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                raise e
        
        return Response(serializer.errors)