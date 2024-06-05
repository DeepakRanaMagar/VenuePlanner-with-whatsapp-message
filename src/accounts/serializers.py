from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class VenueRegistrationSerializer(serializers.Serializer):
    '''
        handles the serialization for the data incoming from the request
    '''

    organization_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_num = serializers.IntegerField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, data):
        '''
            Handles the validation for the password, email and username
        '''

        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Passwords did not match!")

        if User.objects.filter(email=data.get("email")).exists():
            raise serializers.ValidationError("Email is already used!")

        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Username is already taken!")
        
        return data