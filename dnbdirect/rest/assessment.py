from . import request_product

import json

def get_triple_play(duns, auth_token):
    return request_product(auth_token, duns, 'TP_STD', "5.0")

def get_triple_play_composite_score(duns, auth_token):
    try:
        print "Getting triply play..."
        tps = get_triple_play(duns, auth_token)
        print tps
        json_tps = json.loads(tps)
        print json_tps
        return json_tps['OrderProductResponse']['OrderProductResponseDetail']['Product']['Organization']['Assessment']['TriplePlayScore']['CompositeRiskScore']
    except:

        print sys.exc_info()[0]
        return None

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

def get_pbpre(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns)

def get_pbpre_enhanced(duns, auth_token):
    product_code = 'PBPR_ENH'
    return request_product(auth_token, duns, product_code, '3.0')

def get_rating_and_trend(duns, auth_token):
    product_code = 'RTNG_TRND'
    return request_product(auth_token, duns, product_code, "5.0")

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