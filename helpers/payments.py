import requests
import json

from helpers.constants import headers, mockBillingAddress
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def getPaymentToken(order):
    url = f"{STORE_API_URL}/v3/payments/access_tokens"

    payload = {
      "order": {
        "id": order["id"],
        "is_recurring": False
      }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['data']

def processPayment(token, paymentMethod):
    url = f"{PAYMENTS_API_URL}/payments"

    localHeaders = headers.copy()
    localHeaders["Accept"] = "application/vnd.bc.v1+json"
    localHeaders["Authorization"] = f"PAT {token['id']}"

    payload = {
      "payment": paymentMethod
    }
    response = requests.post(url, headers=localHeaders, data=json.dumps(payload))
    return response.json()

# def getPaymentMethods():
#     url = f"{STORE_API_URL}/v2/payments/methods"
#     response = requests.get(url, headers=headers)
#     print(response.json())
