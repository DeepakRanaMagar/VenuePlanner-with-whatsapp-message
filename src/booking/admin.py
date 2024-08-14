from django.contrib import admin

from .models import BookingInfo


@admin.register(BookingInfo)
class BookingInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'venue', 'date', 'status','request_sent_date', 'request_accepted_date', 'request_rejected_date']