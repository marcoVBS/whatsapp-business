from decouple import config
import requests
import json

class WhatsAppAPI:

    def __init__(self) -> None:
        self.__token = config('WHATSAPP_ACCESS_TOKEN')
        self.__phone_id = config('WHATSAPP_PHONE_ID')
        self.__url = config('WHATSAPP_API_URL')

    def send_message(self, recipient, message) -> None:
        url = f"{self.__url}{self.__phone_id}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient,
            "type": "text",
            "text": {
                "body": message,
                "preview_url": False
            }
        }

        return requests.post(url=url, json=payload, headers={"Authorization": f"Bearer {self.__token}"}).json()