__author__ = 'reedn'

import urllib2
import json

def get_auth_token(username, password):
    auth_url = 'https://maxcvservices.dnb.com/rest/Authentication'
    req = urllib2.Request(auth_url)
    req.add_header('x-dnb-user', username)
    req.add_header('x-dnb-pwd', password)
    resp = urllib2.urlopen(req)
    auth_token = resp.info().getheader("Authorization")
    return auth_token

def get_pbpre(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns)

def request_product(auth_token, duns, product_code, version='3.1'):
    url = 'https://maxcvservices.dnb.com/V' + version + '/organizations/' + duns + '/products/' + product_code
    url += "?OrderReasonCode=6332"
    print "Retrieving " + url
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content


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

def get_viability_rating(duns, auth_token):
    product_code = 'VIAB_RAT'
    return request_product(auth_token, duns, product_code, '3.0')

def extract_viability_score_from_viab_rat(viab_rat):
    return json.loads(viab_rat)['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['DNBViabilityRating']['ViabilityScore']['ClassScore']

def get_viability_score(duns, auth_token):
    return extract_viability_score_from_viab_rat(get_viability_rating(duns, auth_token))

def get_pbpre_enhanced(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns, product_code, '3.0')

def get_sers(duns, auth_token):
    pbpre = get_pbpre_enhanced(duns, auth_token)
    return json.loads(pbpre)['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['SupplierEvaluationRiskScore'][0]['RiskScore']

def get_fss(duns, auth_token):
    print "----- get_fss -------"
    product_code = 'PBR_FSS_V7.1'
    obj = json.loads(request_product(auth_token, duns, product_code, '3.0'))
    print obj
    raw_score = obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['FinancialStressScore'][0]['RawScore']
    class_score = obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['FinancialStressScore'][0]['ClassScore']
    return [raw_score, class_score]

def get_fin_st_plus(duns, auth_token):
    url = 'https://maxcvservices.dnb.com/V3.0/organizations/' + duns + '/products/FIN_ST_PLUS'
    url += "?OrderReasonCode=6332"
    print "Retrieving " + url
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content