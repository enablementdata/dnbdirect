from . import order_product

def get_financial_product(duns, product_code):
    return order_product(duns, product_code, "file:/Users/reedn/SOAP/V3.1/FinancialProductService.wsdl")

def get_financial_statement(duns):
    return get_financial_product(duns, "FIN_ST_PLUS")

def read_balance_sheet(response):
    return response.OrderProductResponseDetail.Product.Organization.Financial.FinancialStatement[0].BalanceSheet

def read_total_assets(balance_sheet):
    return balance_sheet.TotalAssetsAmount.value

def read_total_liabilities(balance_sheet):
    return balance_sheet.TotalLiabilitiesAmount.value

def read_profit_and_loss(response):
    return response.OrderProductResponseDetail.Product.Organization.Financial.FinancialStatement[0].ProfitAndLossStatement

def read_sales_from_pnl(pnl):
    return pnl.StatementItem[0].ItemAmount

def read_net_income_from_pnl(pnl):
    return pnl.StatementItem[2].ItemAmount



