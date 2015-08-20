from . import request_product

def get_suits_liens_judgements_and_bankruptcy(duns, auth_token):
    return request_product(auth_token, duns, "PUBREC_DTLS", "3.0")

def get_ucc_filings(duns, auth_token):
    return request_product(auth_token, duns, "PUBREC_UCC", "3.0")
