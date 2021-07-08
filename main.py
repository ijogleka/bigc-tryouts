import requests
import json
import sys

from helpers.products import getCategory, getProductsInCategory
from helpers.customers import getCustomer
from helpers.payments import getPaymentToken, processPayment
from helpers.checkouts import getCheckout, addCheckoutBillingAddress, addCouponToCheckout, getOrderFromCheckout
from helpers.orders import createOrder, markOrderAsPaid
from helpers.carts import createCart

from helpers.constants import headers, mockBillingAddress, mockBillingAddress2
from helpers.constants import testStripePaymentMethod
from helpers.constants import STORE_API_URL, PAYMENTS_API_URL

def workflow_no_cart_purchase_products_with_stripe(product_type, customer_email):
    # Get all products corresponding to the product_type
    categoryProducts = getProductsInCategory(getCategory(product_type))

    # Get the Customer from the Email Address
    customer = getCustomer(customer_email)

    # Construct products for adding to the order
    products = [{
        "product_id": product['id'],
        "quantity": 1,
        "price_inc_tax": 4, # Optional to customize the price. Else uses configured product price
        "price_ex_tax": 3.5, # Optional to customize the price. Else uses configured product price
    } for product in categoryProducts]

    # Create Order
    order = createOrder(products, customer, 'Stripe')

    # Process Payment for the Order
    paymentToken = getPaymentToken(order)
    processPayment(paymentToken, testStripePaymentMethod)


def workflow_cart_checkout_pay_with_stripe(product_type, customer_email):
    # Get all products corresponding to the product_type
    categoryProducts = getProductsInCategory(getCategory(product_type))

    # Get the Customer from the Email Address
    customer = getCustomer(customer_email)

    # Construct product line items for adding to the cart
    products = [{
        "quantity": 1,
        "product_id": product['id'],
    } for product in categoryProducts]

    # Create Cart
    cart = createCart(products, customer)

    # Go through the Checkout Steps
    checkout = getCheckout(cart)
    checkout = addCheckoutBillingAddress(checkout, mockBillingAddress2)
    checkout = addCouponToCheckout(checkout, "LWY50D8GOI")

    # Get Order from Checkout
    order = getOrderFromCheckout(checkout)

    # Process Payment for the Order
    paymentToken = getPaymentToken(order)
    processPayment(paymentToken, testStripePaymentMethod)

def workflow_no_cart_purchase_with_manual(product_type, customer_email):
    # Get all products corresponding to the product_type
    categoryProducts = getProductsInCategory(getCategory(product_type))

    # Get the Customer from the Email Address
    customer = getCustomer(customer_email)

    # Construct products for adding to the order
    products = [{
        "product_id": product['id'],
        "quantity": 1,
        "price_inc_tax": 4, # Optional to customize the price. Else uses configured product price
        "price_ex_tax": 3.5, # Optional to customize the price. Else uses configured product price
    } for product in categoryProducts]

    # Create Order
    order = createOrder(products, customer, 'Manual')

    order = markOrderAsPaid(order)
    return order

def main():
    args = sys.argv[1:]
    if args[0] == 'no_cart_stripe':
        workflow_no_cart_purchase_products_with_stripe(
            product_type="digital-ads",
            customer_email="ijoglekar@gmail.com"
        )
    elif args[0] == 'cart_stripe':
        workflow_cart_checkout_pay_with_stripe(
            product_type="digital-ads",
            customer_email="ijoglekar@gmail.com"
        )
    elif args[0] == 'no_cart_manual':
        workflow_no_cart_purchase_with_manual(
            product_type="digital-ads",
            customer_email="ijoglekar@gmail.com"
        )

main()



'''
Get Products for a product type

Select the first product and create a cart

Start Checkout

Get available payment methods

Add user billing details to the order

Checkout using Stripe
'''
