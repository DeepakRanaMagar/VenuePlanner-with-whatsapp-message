from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from .models import Customer, Venue


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
    terms_condition = serializers.BooleanField()

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
        
        if data.get("terms_condition") is None or data.get("terms_condition") == False:
            raise serializers.ValidationError("Terms & Conditions must be accepted!")
        
        return data
    
    @transaction.atomic
    def save(self):
        try:
            user = User.objects.create(
                email=self.validated_data["email"],
                username=self.validated_data["username"],
                password=make_password(self.validated_data["password"]),
            )
            
            Venue.objects.create(
                user=user,
                organization_name = self.validated_data["organization_name"],
                phone_num = self.validated_data["phone_num"],
                terms_condition = self.validated_data["terms_condition"]
            )
        except Exception as e:
            raise e 
        

class CustomerRegistrationSerializer(serializers.Serializer):
    '''
        handles the serialization for the data incoming from the request
    '''

    full_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    phone_num = serializers.IntegerField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    terms_condition = serializers.BooleanField()

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
    
    @transaction.atomic
    def save(self):
        try:
            user = User.objects.create(
                email=self.validated_data["email"],
                username=self.validated_data["username"],
                password=make_password(self.validated_data["password"]),
            )
            
            Customer.objects.create(
                user=user,
                full_name = self.validated_data["full_name"],
                phone_num = self.validated_data["phone_num"],
                terms_condition = self.validated_data["terms_condition"]
            )
        except Exception as e:
            raise e
        


class UpdateProfileSerializer(serializers.Serializer):
    '''
        Handles the serialization for the fields, to update the profile
    '''
    pan_no = serializers.CharField(required=False)
    # photo1 = serializers.ImageField(required=False)
    # video1 = serializers.FileField(required=False)
    # property_type = serializers.CharField(required=False)


    @transaction.atomic
    def save(self, customer):
        try:
            if 'pan_no' in self.validated_data['pan_no']:
                customer.pan_no = self.validated_data['pan_no']
                print(customer.pan_no)
        except Exception as e:
            raise e


