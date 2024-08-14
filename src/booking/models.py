from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import Customer, Venue


# Create your models here.
class BookingInfo(models.Model):
    '''
        Handles the Booking Detail schema
    '''
    booking_status = [
        # VALUE , KEY
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
    ]

    customer  = models.ForeignKey(Customer, related_name='booking_details',verbose_name=_("Customer"), on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue,related_name="request_details",verbose_name=_("Venue"), on_delete=models.CASCADE)
    date = models.DateField(_("Booking Date"), auto_now=False, auto_now_add=False)
    status = models.CharField(_("status"), choices=booking_status, max_length=50, default='PENDING')
    request_sent_date = models.DateTimeField(_("Request Sent Date"), auto_now_add=True)
    request_accepted_date = models.DateTimeField(_("Request Accepted Date"), null=True, blank=True)
    request_rejected_date = models.DateTimeField(_("Request Rejected Date"), null=True, blank=True, auto_now=False, auto_now_add=False)


    class Meta:
        managed = True
        verbose_name = 'BookingInfo'
        verbose_name_plural = 'BookingInfos'
