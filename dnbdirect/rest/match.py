from urllib import urlencode
from . import retrieve_content_from_url

def extract_matches_from_response_obj(obj):
    return obj['MatchResponse']['MatchResponseDetail']['MatchCandidate']

def extract_confidence_code_from_match(match):
    return match['MatchQualityInformation']['ConfidenceCodeValue']

def extract_duns_from_match(match):
    return match['DUNSNumber']

def extract_company_name_from_match(match):
    return match['OrganizationPrimaryName']['OrganizationName']['$']

def extract_street_from_match(match):
    print "Got into the fucking function!!!!!!"
    try:
        return match['PrimaryAddress']['StreetAddressLine'][0]['LineText']
    except:
        return None

def extract_country_from_match(match):
    try:
        return match['PrimaryAddress']['CountryISOAlpha2Code']
    except:
        return None

def extract_postal_from_match(match):
    try:
        return match['PrimaryAddress']['PostalCode']
    except:
        return None

def extract_city_from_match(match):
    try:
        return match['PrimaryAddress']['PrimaryTownName']
    except:
        return None

def extract_state_from_match(match):
    try:
        return match['PrimaryAddress']['TerritoryAbbreviatedName']
    except:
        return None

def get_matches(auth_token, confidence_code=5, **kwargs):
    query = {'ConfidenceLowerLevelThresholdValue' : confidence_code,
             'match' : 'true',
             'MatchTypeText' : 'Advanced',
             'CountryISOAlpha2Code' : 'US'}

    if kwargs.get('company_name'):
        query['SubjectName'] = kwargs['company_name']
    if kwargs.get('city'):
        query['PrimaryTownName'] = kwargs['city']
    if kwargs.get('state'):
        query['TerritoryName'] = kwargs['state']
    if kwargs.get('postal_code'):
        query['FullPostalCode'] = kwargs['postal_code']
    if kwargs.get('country'):
        query['CountryISOAlpha2Code'] = kwargs['country']

    query_string = urlencode(query)
    url = 'https://maxcvservices.dnb.com/V5.0/organizations?' + query_string
    print url

    return retrieve_content_from_url(auth_token, url)
