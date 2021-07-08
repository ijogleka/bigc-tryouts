import requests
import json

from helpers.constants import headers, mockBillingAddress
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def getCheckout(cart):
    url = f"{STORE_API_URL}/v3/checkouts/{cart['id']}"

    response = requests.get(url, headers=headers)
    return response.json()['data']

def addCheckoutBillingAddress(checkout, billingAddress):
    url = f"{STORE_API_URL}/v3/checkouts/{checkout['id']}/billing-address"

    payload = billingAddress

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['data']

def addCouponToCheckout(checkout, couponCode):
    url = f"{STORE_API_URL}/v3/checkouts/{checkout['id']}/coupons"

    payload = {
        "coupon_code": couponCode
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['data']

def getOrderFromCheckout(checkout):
    url = f"{STORE_API_URL}/v3/checkouts/{checkout['id']}/orders"

    response = requests.post(url, headers=headers)
    return response.json()['data']
