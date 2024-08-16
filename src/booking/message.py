from django.template.loader import render_to_string
from django.conf import settings
import requests
from .models import BookingInfo
# from . import models

def sendWhatsappMessage(phone_num, message):
    message = render_to_string('messages/booking_confirmation.txt', {
        'customer_name': BookingInfo.customer.full_name,
        'venue_name': BookingInfo.venue.organization_name,
        'booking_date': BookingInfo.date,
        # 'booking_status': booking.status,
    })
    
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_num,
        "type": "text",
        "text": {"body":message}
    }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()