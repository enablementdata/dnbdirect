import unittest

from dnbdirect.rest.contacts import get_contacts
from dnbdirect.rest.contacts import extract_job_title_from_contact, extract_management_responsibility_code

from auth import get_auth_token
import json

class ContactsTests(unittest.TestCase):
    def setUp(self):
        self.auth_token = get_auth_token("cpardo@hoovers.com", "dnbdirect123")

    @unittest.skip("testing skipping")
    def test_get(self):
        response = get_contacts(self.auth_token, **{'company_search_term' : 'Dell', 'contacts_search_term' : 'Michael Dell'})
        print response
        self.assertTrue(response)

    @unittest.skip("testing skipping")
    def test_get_for_duns(self):
        response = get_contacts(self.auth_token, **{'contact_search_term' : 'Angie Harper',
                                                    'duns' : '186830733'})
        obj = json.loads(response)
        contacts = obj['FindContactResponse']['FindContactResponseDetail']['FindCandidate']
        print contacts

        self.assertTrue(response)

    @unittest.skip("testing skipping")
    def test_get_for_email(self):
        response = get_contacts(self.auth_token, **{'contact_email' : 'jnoronha@eogresources.com'})
        obj = json.loads(response)
        contacts = obj['FindContactResponse']['FindContactResponseDetail']['FindCandidate']
        print contacts
        self.assertEqual(1, len(contacts))

    @unittest.skip("testing skipping")
    def test_extract_job_title_from_contact(self):
        response = get_contacts(self.auth_token, **{'contact_email' : 'jnoronha@eogresources.com'})
        obj = json.loads(response)
        contacts = obj['FindContactResponse']['FindContactResponseDetail']['FindCandidate']
        contact = contacts[0]
        self.assertEqual("Information Technology Manager", extract_job_title_from_contact(contact))

    def test_extract_management_responsibility_code(self):
        response = get_contacts(self.auth_token, **{'contact_email' : 'chris.collins@workday.com', 'duns' : '607009755'})
        obj = json.loads(response)
        contacts = obj['FindContactResponse']['FindContactResponseDetail']['FindCandidate']
        contact = contacts[0]
        self.assertEqual("Manager", extract_management_responsibility_code(contact))