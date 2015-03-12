from suds.client import Client
from suds.wsse import *

def get_client():
    client = Client("file:/Users/reedn/SOAP/LinkageService/V3.1/LinkageService.wsdl")
    security = Security()
    token = UsernameToken('cpardo@hoovers.com', 'dnbdirect123')
    security.tokens.append(token)
    client.set_options(wsse=security, retxml=True)
    return client

def order_product(duns, product_code):
    client = get_client()
    order_product_request_detail = client.factory.create("OrderProductRequestDetail")
    order_product_request_detail.InquiryDetail.DUNSNumber = duns
    order_product_request_detail.ProductSpecification.DNBProductID = product_code
    request_transaction_detail = client.factory.create("RequestTransactionDetail")

    response = client.service.OrderProduct(request_transaction_detail, order_product_request_detail)
    return response

def get_family_tree_enhanced(duns):
    return order_product(duns, "LNK_FF")

def get_family_tree_standard(duns):
    return order_product(duns, "LNK_UPF")

