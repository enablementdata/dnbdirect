__author__ = 'reedn'

import urllib2, urllib
import json
import sys

def retrieve_content_from_url(auth_token, url):
    req = urllib2.Request(url)
    req.add_header('Authorization', auth_token)
    resp = urllib2.urlopen(req)
    content = resp.read()
    return content

# Returns string content from product request
def request_product(auth_token, duns, product_code, version='3.1', reason_code='6332'):
    print "--- request_product"
    print "Auth_Token: "
    print auth_token
    print "Duns: "
    print duns
    print "Product code: "
    print product_code

    try:
        url = 'https://maxcvservices.dnb.com/V' + version + '/organizations/' + duns + '/products/' + product_code
        if reason_code:
            url += "?OrderReasonCode=6332"
        print "------ Retrieving " + url
        content = retrieve_content_from_url(auth_token, url)
        return content
    except urllib2.HTTPError, e:
        print e
    except:
        print sys.exc_info()[0]
        return "{}"

def get_entity_match(company_name, auth_token):
    query = urllib.urlencode({"SubjectName": company_name, "match" : "true", "CountryISOAlpha2Code" : "US"})
    url = "https://maxcvservices.dnb.com/V4.0/organizations?" + query
    print url
    content = retrieve_content_from_url(auth_token, url)
    print content
    return json.loads(content)