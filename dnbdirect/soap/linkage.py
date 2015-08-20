from . import order_product

def get_family_tree(duns, product_code):
    return order_product(duns, product_code, "file:/Users/reedn/SOAP/LinkageService/V3.1/LinkageService.wsdl")

def get_family_tree_enhanced(duns):
    return get_family_tree(duns, "LNK_FF")

def get_family_tree_standard(duns):
    return get_family_tree(duns, "LNK_UPF")

def read_global_ultimate_duns(response):
    return response.OrderProductResponseDetail.Product.Organization.Linkage.GlobalUltimateOrganization.DUNSNumber

def read_child_quantity(response):
    return response.OrderProductResponseDetail.Product.Organization.Linkage.LinkageSummary.ChildrenSummary[0].ChildrenQuantity


