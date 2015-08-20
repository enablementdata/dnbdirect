import json

from . import request_product

def get_dcp_standard(duns, auth_token):
    product_code = 'DCP_STD'
    return request_product(auth_token, duns, product_code)

def get_dcp_premium(duns, auth_token):
    product_code = 'DCP_PREM'
    return request_product(auth_token, duns, product_code)

def get_dcp_enhanced(duns, auth_token):
    product_code = 'DCP_ENH'
    return request_product(auth_token, duns, product_code)

def get_commercial_credit_score(duns, auth_token):
    dcp = get_dcp_premium(duns, auth_token)
    return extract_commercial_credit_score_from_dcp(dcp)

def extract_commercial_credit_score_from_dcp(dcp):
    json_dcp = json.loads(dcp)
    text = json_dcp['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['CommercialCreditScore'][0]['MarketingRiskClassText']['$']
    code_value = json_dcp['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['CommercialCreditScore'][0]['MarketingRiskClassText']['@DNBCodeValue']
    return [text, code_value]
