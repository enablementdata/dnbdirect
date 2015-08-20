from urllib import urlencode
from . import retrieve_content_from_url
import json

import logging

def extract_contacts_from_response(response):
    obj = json.loads(response)
    contacts = obj['FindContactResponse']['FindContactResponseDetail']['FindCandidate']
    return contacts

def extract_job_title_from_contact(contact):
    try:
        return contact['JobTitle'][0]['JobTitleText']['$']
    except:
        return None

def extract_management_responsibility_code(contact):
    try:
        return contact['ManagementResponsibilityCodeText'][0]['$']
    except:
        return None

def get_contacts(auth_token, **kwargs):
    logging.debug("--- get_contacts ---")

    query = {'findcontact' : 'true',
             'SearchModeDescription' : 'Basic'}

    if kwargs.get('contacts_search_term'):
        query['KeywordContactText'] = kwargs.get('contacts_search_term')
    if kwargs.get('company_search_term'):
        query['KeywordText'] = kwargs.get('company_search_term')
    if kwargs.get('duns'):
        query['DUNSNumber'] = kwargs['duns']
        query['SearchModeDescription'] = 'Advanced'
    if kwargs.get("contact_email"):
        query['ContactEmailAddress'] = kwargs['contact_email']
        query['SearchModeDescription'] = 'EmailLookup'

    url = 'https://maxcvservices.dnb.com/V6.1/organizations?%s' % urlencode(query)
    logging.debug(url)
    print url
    print auth_token
    return retrieve_content_from_url(auth_token, url)

