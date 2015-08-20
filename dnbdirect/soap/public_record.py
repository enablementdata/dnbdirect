from . import order_product

def get_public_record(duns, product_code):
    return order_product(duns, product_code, "File:/Users/reedn/SOAP/PublicRecordProductService/V3.0/PublicRecordProductService.wsdl")

def get_suits(duns):
    return get_public_record(duns, "PUBREC_SUITS")

def get_liens(duns):
    return get_public_record(duns, "PUBREC_LIENS")

def get_judgements(duns):
    return get_public_record(duns, "PUBREC_JDG")

def get_suits_liens_judgements_and_bankruptcy(duns):
    return get_public_record(duns, "PUBREC_DTLS")

def get_ucc_filings(duns):
    return get_public_record(duns, "PUBREC_UCC")

def read_liens_indicator(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.LiensIndicator

def read_judgements_indicator(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.JudgmentIndicator

def read_suits_indicator(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.SuitsIndicator

def read_judgements_total_filing_count(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.JudgmentInformation.JudgmentSummary.TotalFilingCount

def read_suits_total_filing_count(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.SuitInformation.SuitSummary[0].TotalFilingCount

def read_liens_filing_count(response):
    return response.OrderProductResponseDetail.Product.Organization.Events.LegalEvents.LienInformation.LienSummary.TotalFilingCount