from requests_futures.sessions import FuturesSession

import json

def request_product(auth_token, duns, product_code, version='3.1'):
    session = FuturesSession()
    url = 'https://maxcvservices.dnb.com/V' + version + '/organizations/' + duns + '/products/' + product_code
    url += "?OrderReasonCode=6332"
    print url
    headers = {'Authorization': auth_token}
    future = session.get(url, headers=headers)
    return future

def get_dcp_premium(duns, auth_token):
    product_code = 'DCP_PREM'
    return request_product(auth_token, duns, product_code)

def get_pbpre(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns)

def get_dcp_enhanced(duns, auth_token):
    product_code = 'DCP_ENH'
    return request_product(auth_token, duns, product_code)

def get_commercial_credit_score(duns, auth_token):
    dcp = get_dcp_premium(duns, auth_token)
    return extract_commercial_credit_score_from_dcp(dcp)

def extract_commercial_credit_score_from_dcp(dcp):
    pass

def get_triple_play(duns, auth_token):
    return request_product(auth_token, duns, 'TP_STD', "5.0")


def read_fss_from_response(duns, response):
    obj = json.loads(response.content)
    print obj
    raw_score = None
    class_score = None
    try:
        raw_score = obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment'][
            'FinancialStressScore'][0]['RawScore']
    except:
        print "Warning: Missing FSS raw score for " + duns
    try:
        class_score = \
        obj['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment'][
            'FinancialStressScore'][0]['ClassScore']
    except:
        print "Warning: Missing FSS class score for " + duns
    return [raw_score, class_score]


def get_fss(duns, auth_token):
    product_code = 'PBR_FSS_V7.1'
    future = request_product(auth_token, duns, product_code, '3.0')
    return future

