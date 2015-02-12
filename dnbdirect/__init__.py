__author__ = 'reedn'

import urllib2, urllib
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


def retrieve_content_from_url(auth_token, url):
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content

# Returns string content from product request
def request_product(auth_token, duns, product_code, version='3.1'):
    try:
        url = 'https://maxcvservices.dnb.com/V' + version + '/organizations/' + duns + '/products/' + product_code
        url += "?OrderReasonCode=6332"
        print "Retrieving " + url
        content = retrieve_content_from_url(auth_token, url)
        return content
    except:
        return "{}"

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
    text = None
    code_value = None
    try:
        text = json_dcp['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['CommercialCreditScore'][0]['MarketingRiskClassText']['$']
    except:
        print "Warning: Missing text of CommericalCreditScore"

    try:
        code_value = json_dcp['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['CommercialCreditScore'][0]['MarketingRiskClassText']['@DNBCodeValue']
    except:
        print "Warning: Missing CommercialCreditScore code_value"

    return [text, code_value]

def get_viability_rating(duns, auth_token):
    product_code = 'VIAB_RAT'
    return request_product(auth_token, duns, product_code, '3.0')

def extract_viability_score_from_viab_rat(viab_rat):
    try:
        viability_score = json.loads(viab_rat)['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['DNBViabilityRating']['ViabilityScore']['ClassScore']
        return viability_score
    except:
        return None

def get_viability_score(duns, auth_token):
    return extract_viability_score_from_viab_rat(get_viability_rating(duns, auth_token))

def get_pbpre_enhanced(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns, product_code, '3.0')

def get_sers(duns, auth_token):
    pbpre = get_pbpre_enhanced(duns, auth_token)
    try:
        sers = json.loads(pbpre)['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['SupplierEvaluationRiskScore'][0]['RiskScore']
        return sers
    except:
        return None

def get_fss(duns, auth_token):
    print "----- get_fss -------"
    product_code = 'PBR_FSS_V7.1'
    obj = json.loads(request_product(auth_token, duns, product_code, '3.0'))
    print obj
    raw_score = None
    class_score = None
    try:
        raw_score = obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['FinancialStressScore'][0]['RawScore']
    except:
        print "Warning: Missing FSS raw score for " + duns

    try:
        class_score = obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['FinancialStressScore'][0]['ClassScore']
    except:
        print "Warning: Missing FSS class score for " + duns
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

def get_entity_match(company_name, auth_token):
    query = urllib.urlencode({"SubjectName": company_name, "match" : "true", "CountryISOAlpha2Code" : "US"})
    url = "https://maxcvservices.dnb.com/V4.0/organizations?" + query
    print url
    content = retrieve_content_from_url(auth_token, url)
    print content
    return json.loads(content)