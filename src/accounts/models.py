from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from nepali_address.models import District, Municipality, Province


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("auth user"), on_delete=models.CASCADE)
    phone_num = models.IntegerField(_("phone number"), unique=True)
    terms_condition = models.BooleanField(_("Terms & Condition"), default=False)

    class Meta:
        abstract = True


property_type = {
    # "Value" : "Key"
    "Party Palace" : "Party Palace",
    "Resort" : "Resort", 
    "Restaurant" : "Restaurant",
    "Lounge" : "Lounge",
    "Community Hall" : "Community Hall",
    "Office Space" : "Office Space",
}


class Venue(UserProfile):
    '''
        Handles the Schema for the Venue Model
    '''
    organization_name = models.CharField(_("organization name"), max_length=50)

    #Edit profile fields
    pan_no = models.CharField(_("Pan Number"),max_length=9, blank=True, null=True)
    
    #property fields
    property_type = models.CharField(_("Property Type"), choices=property_type, max_length=50, null=True, blank=True)
    
    #media fields
    photo1 = models.ImageField(_("Photo 1 "), upload_to='images/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    video1 = models.FileField(_("Video 1"), upload_to='videos/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])], blank=True, null=True)
    
    #address fields
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    municipality = models.ForeignKey(Municipality, on_delete=models.SET_NULL, null=True, blank=True)
    ward = models.IntegerField(null=True, blank=True)    
    
    def __str__(self):
        return self.user.username
    
class Customer(UserProfile):
    '''
        Handles the Schema for the Customer Model
    '''
    full_name = models.CharField(_("Full name"), max_length=50)

    def __str__(self):
        return self.user.username
    