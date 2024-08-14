from django.contrib.auth.models import User
from django.core.validators import (FileExtensionValidator, MaxValueValidator,
                                    MinValueValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _
from nepali_address.models import District, Municipality, Province


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("auth user"), on_delete=models.CASCADE)
    phone_num = models.IntegerField(_("phone number"), unique=True)
    terms_condition = models.BooleanField(_("Terms & Condition"), default=False)

    class Meta:
        abstract = True



class Venue(UserProfile):
    '''
        Handles the Schema for the Venue Model
    '''
    property_type = {
        # "Value" : "Key"
        "Party Palace" : "Party Palace",
        "Resort" : "Resort", 
        "Restaurant" : "Restaurant",
        "Lounge" : "Lounge",
        "Community Hall" : "Community Hall",
        "Office Space" : "Office Space",
    }

    organization_name = models.CharField(_("organization name"), max_length=50)

    #Edit profile fields
    pan_no = models.CharField(_("Pan Number"),max_length=9, blank=True, null=True)
    
    # Logo field
    logo = models.ImageField(_("Venue logo"), upload_to='images/logo',null=True, blank=True, height_field=None, width_field=None, max_length=None)

    #property fields
    property_type = models.CharField(_("Property Type"), choices=property_type, max_length=50, null=True, blank=True)
    
    #media fields
    photo1 = models.ImageField(_("Photo 1 "), upload_to='images/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    video1 = models.FileField(_("Video 1"), upload_to='videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True, null=True)
    
    #address fields
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True)
    ward = models.IntegerField(null=True, blank=True)    

    # address = models.CharField(_("Venue Address"), max_length=50, null=True, blank=True)
    
    #subscription
    isSubscribed = models.BooleanField(default=False)

    #subscribed media
    photo2 = models.ImageField(_("Subscription Photo"), upload_to='images/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    video2 = models.FileField(_("Subscription Video"), upload_to='videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True, null=True)

    #social media 
    social1 = models.URLField(_("URL 1"), max_length=200, blank=True, null=True)
    social2 = models.URLField(_("URL 2"), max_length=200, blank=True, null=True)
    social3 = models.URLField(_("URL 3"), max_length=200, blank=True, null=True)

    # rating
    rating = models.IntegerField(_("Rating"), validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

    # pricing
    price = models.IntegerField(_("Price"), validators=[MinValueValidator(0)], null=True, blank=True)

    # seat capacity 
    seat_capacity = models.IntegerField(_("Seat Capacity"), null=True, blank=True)



    def __str__(self):
        return self.user.username
    

class Media(models.Model):
    '''
        Handles model schema for the Media Files uploaded for the Venue
    '''
    venue = models.ForeignKey(Venue, verbose_name=_("venue"), on_delete=models.CASCADE)

    photo = models.ImageField(_("Subscription photo"), upload_to='images/subscription/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    video = models.FileField(_("Subscription video"), upload_to='videos/subscription/', max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return f'Photo for {self.venue.organization_name}'

class Customer(UserProfile):
    '''
        Handles the Schema for the Customer Model
    '''
    full_name = models.CharField(_("Full name"), max_length=50)

    def __str__(self):
        return self.user.username
    
