from . import request_product

def get_business_background_report(duns, auth_token):
    return request_product(auth_token, duns, 'BBR', "3.0", None)

