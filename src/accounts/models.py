from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("auth user"), on_delete=models.CASCADE)
    phone_num = models.IntegerField(_("phone number"))
    terms_condition = models.BooleanField(_("Terms & Condition"), default=False)

    class Meta:
        abstract = True

class Venue(UserProfile):
    '''
        Handles the Schema for the Venue Model
    '''
    organization_name = models.CharField(_("organization name"), max_length=50)

    def __str__(self):
        return self.user.username
    
class Customer(UserProfile):
    '''
        Handles the Schema for the Customer Model
    '''
    full_name = models.CharField(_("Full name"), max_length=50)

    def __str__(self):
        return self.user.username
    