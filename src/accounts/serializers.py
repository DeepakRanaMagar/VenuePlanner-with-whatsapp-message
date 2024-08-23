from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers

from .models import Customer, Media, Venue


class UserSerializer(serializers.ModelSerializer):
    '''
        Default auth user model serializer
    '''
    class Meta:
        model = User
        # fields = ['email', 'username']
        exclude = ['id', 'first_name', 'last_name', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'date_joined']

class VenueSerializer(serializers.ModelSerializer):
    '''
        Handles the Serialization for the Venue model 
    '''
    user = UserSerializer(read_only = True) #Calls the UserSerializer for the serialization of the user(OneToOne Field) in the model

    class Meta:
        model = Venue
        fields = '__all__'


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
        

class CustomerSerializer(serializers.ModelSerializer):
    '''
        Handles the Serialization for the Customer model 
    '''
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'




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
    organization_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required =False)
    logo = serializers.ImageField(required=False)
    pan_no = serializers.CharField(required=False)
    photo1 = serializers.ImageField(required=False)
    video1 = serializers.FileField(required=False)
    property_type = serializers.CharField(required=False)
    seat_capacity = serializers.CharField(required=False)

    @transaction.atomic
    def save(self, venue):
        # print(self.validated_data['property_type'])
        try:
            
            if 'seat_capacity' in self.validated_data:
                venue.seat_capacity = int(self.validated_data['seat_capacity'])
            
            if 'organization_name' in self.validated_data:
                venue.organization_name = self.validated_data['organization_name']

            if 'email' in self.validated_data:
                venue.user.email = self.validated_data['email']
                venue.user.save()
            
            if 'address' in self.validated_data:
                venue.address = self.validated_data['address']

            if 'logo' in self.validated_data:
                venue.logo =self.validated_data['logo']

            if 'pan_no' in self.validated_data:
                venue.pan_no = self.validated_data['pan_no']
            
            if 'property_type' in self.validated_data:
                type = self.validated_data['property_type']
                # print(type)
                try:
                    venue.property_type = type
                    # print(f"{type} is saved!!!!")
                except Exception as e:
                    raise e
            

            if 'photo1' in self.validated_data:
                venue.photo1 = self.validated_data['photo1']
        
            if 'video1' in self.validated_data:
                venue.video1 = self.validated_data['video1']

            venue.save()
        except Exception as e:
            raise e

class SubscribeSerializer(serializers.Serializer):
    '''
        Handles serialization for the Subscription field of the Venue Model.
    '''
    isSubscribed = serializers.BooleanField(required=True)

    @transaction.atomic
    def save(self, venue):

        try:
            if 'isSubscribed' in self.validated_data:
                value = self.validated_data['isSubscribed']
                # print(value)
                try:
                    venue.isSubscribed = value
                    print("Subscribed DONE")
                except Exception as e:
                    raise e
                venue.save()
        except Exception as e:
            raise e    


class SubPassSerializer(serializers.Serializer):
    '''
        Handles the serializeration for the Subscribed Priviliges
    '''
    photo2 = serializers.ListField(
        child = serializers.ImageField(required=False),
        required = False
    )
    video2 = serializers.ListField(
        child = serializers.FileField(required=False),
        required = False
    )

    # URLS
    social1 = serializers.URLField(required=False)
    social2 = serializers.URLField(required=False)
    social3 = serializers.URLField(required=False)

    @transaction.atomic
    def save(self, venue):
        try:
            if 'photo2' in self.validated_data:
                    for photo in self.validated_data['photo2']:
                        try:
                            Media.objects.create(
                                venue=venue,
                                photo=photo
                            )
                        except Exception as e:
                            raise e
            
            if 'video2' in self.validated_data:
                    for video in self.validated_data['video2']:
                        try:
                            Media.objects.create(
                                venue=venue,
                                video=video
                            )
                        except Exception as e:
                            raise e

            if 'social1' in self.validated_data:
                url1  = self.validated_data['social1']
                # print(url1)
                try: 
                    venue.social1 = url1
                    
                except Exception as e:
                    raise e
            
            if 'social2' in self.validated_data:
                url2  = self.validated_data['social2']
                # print(url1)
                try: 
                    venue.social2 = url2
                    
                except Exception as e:
                    raise 
            
            if 'social3' in self.validated_data:
                url3  = self.validated_data['social3']
                # print(url1)
                try: 
                    venue.social3 = url3
                    
                except Exception as e:
                    raise

            venue.save()

                
        except Exception as e:
            raise e
        



# class MediaSerializer(serializers.ModelSerializer):
#     '''
#         Handles the serialization for the Media Model
#     '''
#     class Meta:
#         model = Media
#         fields = ['photo', 'video']
    
# class VenueSerializer(serializers.ModelSerializer):
#     photos = MediaSerializer(many=True, required=False)
#     videos = MediaSerializer(many=True, required=False)

#     class Meta:
#         model = Venue
#         fields = ['']
