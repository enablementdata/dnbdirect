from dnbdirect.soap import order_product

def get_assessment(duns, product_code):
    return order_product(duns, product_code, "File:/Users/reedn/SOAP/V5.0/AssessmentProductService.wsdl")

def get_rating_and_trend(duns):
    return get_assessment(duns, "RTNG_TRND")

def get_sers(duns):
    return get_assessment(duns, "SER")

def read_sers_risk_score(response):
    return response.OrderProductResponseDetail.Product.Organization.Assessment.SupplierEvaluationRiskScore[0].RiskScore

def read_dnb_standard_rating(response):
    return response.OrderProductResponseDetail.Product.Organization.Assessment.DNBStandardRating.DNBStandardRating

def read_history_rating_text(response):
    return response.OrderProductResponseDetail.Product.Organization.Assessment.HistoryRatingText.value

def read_financial_condition_text(response):
    return response.OrderProductResponseDetail.Product.Organization.Assessment.FinancialConditionText.value

