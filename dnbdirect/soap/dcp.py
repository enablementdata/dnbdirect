from dnbdirect.soap import order_product

def get_dcp(duns, product_code):
    return order_product(duns, product_code, "file:/Users/reedn/SOAP/Firmographics/V3.2_New/FirmographicsProductService.wsdl")

def get_dcp_enhanced(duns):
    return get_dcp(duns, "DCP_ENH")

def get_dcp_premium(duns):
    return get_dcp(duns, "DCP_PREM")

def get_dcp_standard(duns):
    return get_dcp(duns, "DCP_STD")

def read_organization_name(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.OrganizationName.OrganizationPrimaryName[0].OrganizationName

def read_industry_codes(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.IndustryCode

def read_industry_code_text(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.IndustryCode[0][0].IndustryCodeDescription[0].value

def read_industry_code_value(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.IndustryCode[0][0].IndustryCode

def read_individual_employee_quantity(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.EmployeeFigures.IndividualEntityEmployeeDetails.TotalEmployeeQuantity

def read_street_address1(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.Location.PrimaryAddress[0].StreetAddressLine[0].LineText

def read_city(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.Location.PrimaryAddress[0].PrimaryTownName

def read_state(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.Location.PrimaryAddress[0].TerritoryAbbreviatedName

def read_postal_code(dcp):
    return dcp.OrderProductResponseDetail.Product.Organization.Location.PrimaryAddress[0].PostalCode
