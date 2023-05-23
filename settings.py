from os import getenv

STRIPE_CONFIG = {
    "CUSTOMER_DETAIL_ENDPOINT" : getenv("CUSTOMER_DETAIL_ENDPOINT") , 
    "Authorization" : getenv("Authorization_Header")
}