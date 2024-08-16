import requests
from django.conf import settings
from django.template.loader import render_to_string

from .models import BookingInfo


def sendWhatsappMessage(phone_num, message):
    # message = render_to_string('messages/booking_confirmation.txt', {
    #     'customer_name': BookingInfo.customer.full_name,
    #     'venue_name': BookingInfo.venue.organization_name,
    #     'booking_date': BookingInfo.date,
    #     # 'booking_status': booking.status,
    # })
    
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
    return ans

# def sendWhatsappMessage(customer, venue, booking_date):
#     # Prepare context data for the template
#     context = {
#         'customer_name': customer.full_name,
#         'venue_name': venue.organization_name,
#         'booking_date': booking_date,
#     }

#     # Render the template with the provided context
#     message = render_to_string('whatsapp_message.txt', context)

#     # Sending the WhatsApp message
#     headers = {"Authorization": settings.WHATSAPP_TOKEN}
#     payload = {
#         "messaging_product": "whatsapp",
#         "recipient_type": "individual",
#         "to": customer.phone_num,
#         "type": "text",
#         "text": {"body": message}
#     }
#     response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
#     return response.json()