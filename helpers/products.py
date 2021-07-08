import requests

from .constants import headers, mockBillingAddress
from .constants import testStripePaymentMethod
from .constants import STORE_API_URL, PAYMENTS_API_URL

def getCategory(categoryName):
    url = f"{STORE_API_URL}/v3/catalog/categories"
    params = {
        "name": categoryName
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['data'][0]

def getProductsInCategory(category):
    url = f"{STORE_API_URL}/v3/catalog/products"
    params = {
        "categories": [category['id']]
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['data']

# def addMetafieldsToProduct(product):
#     print(product['id'])
#     url = f"{STORE_API_URL}/v3/catalog/products/{product['id']}/metafields"
#     payload = {
#       "permission_set": "app_only",
#       "namespace": "App Namespace",
#       "key": "json_metadata",
#       "value": "{'mock_key': 'mock_value'}",
#       "description": "Digital Ads provided JSON Metadata"
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(payload))
#
# def getProductMetafields(product):
#     url = f"{STORE_API_URL}/v3/catalog/products/{product['id']}/metafields"
#     params = {
#         "namespace": "App Namespace"
#     }
#     response = requests.get(url, headers=headers, params=params)
#     print(response.json()['data'])
