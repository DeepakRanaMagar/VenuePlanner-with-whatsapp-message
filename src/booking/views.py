from django.shortcuts import render

from .serializers import BookingSerializer
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

        # print("data:", data)
        if isCustomer:
            data['customer'] = isCustomer.id
            serializer = BookingSerializer(data=data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    print("serializer data:", serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

