__author__ = 'reedn'

import os

#from .linkage import get_family_tree_enhanced, get_family_tree_standard
#from .dcp import get_dcp_premium, get_dcp_enhanced
#from .fin_st_plus import get_financial_statement
#from .public_record import get_suits_liens_judgements_and_bankruptcy
#from .assessment import get_rating_and_trend, get_ser

from suds.client import Client
from suds.wsse import *

def get_client(wsdl):
    client = Client(wsdl, timeout=180)
    security = Security()
    token = UsernameToken(os.environ['API_USERNAME'], os.environ['API_PASSWORD'])
    security.tokens.append(token)
    client.set_options(wsse=security) # retxml=False)
    return client

def order_product(duns, product_code, wsdl):
    client = get_client(wsdl)
    order_product_request_detail = client.factory.create("OrderProductRequestDetail")
    order_product_request_detail.InquiryDetail.DUNSNumber = duns
    order_product_request_detail.ProductSpecification.DNBProductID = product_code
    request_transaction_detail = client.factory.create("RequestTransactionDetail")

    response = client.service.OrderProduct(request_transaction_detail, order_product_request_detail)
    return response

