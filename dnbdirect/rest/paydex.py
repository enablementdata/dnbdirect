from . import request_product

def get_paydex_premium(duns, auth_token):
    return request_product(auth_token, duns, "PIAP_PREM", "4.0")