import urllib2

def get_fin_st_plus(duns, auth_token):
    url = 'https://maxcvservices.dnb.com/V3.0/organizations/' + duns + '/products/FIN_ST_PLUS'
    url += "?OrderReasonCode=6332"
    print "Retrieving " + url
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content