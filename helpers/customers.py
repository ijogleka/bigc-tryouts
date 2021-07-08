import requests

from helpers.constants import headers, mockBillingAddress
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def getCustomer(email):
    url = f"{STORE_API_URL}/v3/customers"
    params = {
        "email:in": email
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['data'][0]
