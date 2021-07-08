import requests
import json

from helpers.constants import headers, mockBillingAddress
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def createOrder(products, customer, paymentMethod):
    url = f"{STORE_API_URL}/v2/orders"
    payload = {
        "products": products,
        "billing_address": mockBillingAddress,
        "customer_id": customer['id'],
        "payment_method": paymentMethod,
        "order_is_digital": True,
        "discount_amount": 0.75,
        "status_id": 0 # https://developer.bigcommerce.com/api-reference/store-management/orders/order-status/getaorderstatus
        # Needs to be set to 0 for API payments
    }
    # Creates a order with the `Incomplete` state
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def markOrderAsPaid(order):
    url = f"{STORE_API_URL}/v2/orders/{order['id']}"

    payload = {
        "status_id": 10,
        "payment_method": "MARQ",
        "payment_provider_id": "marqeta"
    }

    response = requests.put(url, headers=headers, data=json.dumps(payload))
    return response.json()
