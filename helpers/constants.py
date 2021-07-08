import os

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "X-Auth-Token": f"{os.environ.get('BIGC_ACCESS_TOKEN')}", # Access Token
    "Content-Type": "application/json",
    "Accept": "application/json"
}
mockBillingAddress = {
    "first_name": "Key",
    "last_name": "Value",
    "street_1": "10001",
    "city": "Malvern",
    "state": "PA",
    "zip": 19355,
    "country": "United States",
}
mockBillingAddress2 = {
  "first_name": "Key",
  "last_name": "Value",
  "email": "ijoglekar@gmail.com",
  "address1": "123 Main Street",
  "address2": "",
  "city": "Malvern",
  "state_or_province": "Pennsylvania",
  "state_or_province_code": "PA",
  "country_code": "US",
  "postal_code": "19355"
}
testStripePaymentMethod = {
  "instrument": {
    "type": "card",
    "cardholder_name": "Key Value",
    "number": "4111111111111111",
    "expiry_month": 1,
    "expiry_year": 2025,
    "verification_value": "123"
  },
  "payment_method_id": "stripev3.card"
}

STORE_API_URL = f"https://api.bigcommerce.com/stores/{os.environ.get('BIGC_STORE_HASH')}"
PAYMENTS_API_URL = f"https://payments.bigcommerce.com/stores/{os.environ.get('BIGC_STORE_HASH')}"
