from requests_futures.sessions import FuturesSession

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