import requests
import json

from helpers.constants import headers, mockBillingAddress
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def createCart(products, customer):
    url = f"{STORE_API_URL}/v3/carts"

    payload = {
      "line_items": products,
      "customer_id": customer['id']
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['data']
