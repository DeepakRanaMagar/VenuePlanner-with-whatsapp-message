from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Venue
from .serializers import (CustomerRegistrationSerializer, SubPassSerializer,
                          SubscribeSerializer, UpdateProfileSerializer,
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
        

class LogoutView(APIView):
    '''
        Handles the endpoints for the Logout
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(
            {"message": "Successfully logged out"}, status=status.HTTP_200_OK
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
        # print(request.data['property_type'])
        try:
            venue = Venue.objects.get(user=request.user)
            # print(venue)

        except Venue.DoesNotExist as e:
            return Response(
                {
                    f"Account doesn't exists." 
                }, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save(venue=venue)
                return Response(
                    {
                        f"Your profile is successfully updated"
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                raise e
        
        return Response(serializer.errors)
    

class SubscriptionView(APIView):
    '''
        Handles the Endpoint for the Subscription
    '''
    permission_classes = [IsAuthenticated, ]
    
    def post(self, request):
        '''
            Handles post() for the subscription 
        '''
        # print(request.data)
        try:
            venue = Venue.objects.get(user=request.user)
            # print(f'{venue} is present')

        except Venue.DoesNotExist as e:
            return Response(
                {
                    f"Account doesn't exists." 
                }, status=status.HTTP_404_NOT_FOUND
            )
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save(venue=venue)
                return Response(
                    {
                        f"Subscribed is successfully."
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                raise e
        
        return Response(serializer.errors)



class SubPassView(APIView):
    '''
        Handles API Endpoints for the subscribed venue, to access the fields
    '''
    def post(self, request):
        # print(request.data)
        try:
            venue = Venue.objects.get(user=request.user)
            # print(f'{venue} is present')

        except Venue.DoesNotExist as e:
            return Response(
                {
                    f"Account doesn't exists." 
                }, status=status.HTTP_404_NOT_FOUND
            )
        serializer = SubPassSerializer(data=request.data)
        if serializer.is_valid():
            try: 
                serializer.save(venue=venue)
                return Response(
                    {
                        f"Link is successfully posted."
                    }, status=status.HTTP_200_OK
                )
            except Exception as e:
                raise e
        
        return Response(serializer.errors)
