import requests
from django.conf import settings
from decouple import config


def sendWhatsappMessage(phone_num, message):
    
    # url = settings.WHATSAPP_URL
    url = config('WHATSAPP_URL')
    token = config('WHATSAPP_TOKEN')

    if not url:
        print("url: ",url)
        raise ValueError("WHATSAPP_URL is not configured or is empty.")
    if not token:
        print('token: ', token)
        raise ValueError("WHATSAPP_TOKEN is not configured or is empty.")

    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_num,
        "type": "text",
        "text": {
            "preview_url": True,
            "body":message
            }
    }
    # Check if URL is correctly configured
    # if not url:
    #     raise ValueError("WHATSAPP_URL is not configured in settings.py")

    # Make the POST request
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending WhatsApp message: {e}")
        

# phone_num = 9867288665
# message = "Hello this is test message"
# sendWhatsappMessage(phone_num, message)
