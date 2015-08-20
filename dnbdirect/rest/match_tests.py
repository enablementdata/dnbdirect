import json
import unittest

from match import get_matches, extract_street_from_match, extract_city_from_match, extract_country_from_match, extract_company_name_from_match, extract_confidence_code_from_match, extract_matches_from_response_obj, extract_postal_from_match, extract_duns_from_match, extract_state_from_match
from auth import get_auth_token

class MatchTests(unittest.TestCase):
    def setUp(self):
        self.auth_token = get_auth_token("cpardo@hoovers.com", "dnbdirect123")
        self.matches = self.read_matches()

    def read_matches(self):
        with open("match_example_response.txt", "r") as f:
            return extract_matches_from_response_obj(json.loads(f.read()))

    def test_extract_company_name_from_match(self):
        self.assertEqual("DELL INC.", extract_company_name_from_match(self.matches[0]))

    def test_extract_street_from_match(self):
        self.assertEqual("1 DELL WAY", extract_street_from_match(self.matches[0]))

    def test_extract_country_from_match(self):
        self.assertEqual("US", extract_country_from_match(self.matches[0]))

    def test_extract_postal_from_match(self):
        self.assertEqual("78682", extract_postal_from_match(self.matches[0]))

    def test_extract_city_from_match(self):
        self.assertEqual("ROUND ROCK", extract_city_from_match(self.matches[0]))

    def test_extract_confidence_code_from_match(self):
        self.assertEqual(7, extract_confidence_code_from_match(self.matches[0]))

    def test_extract_duns_from_match(self):
        self.assertEqual("114315195", extract_duns_from_match(self.matches[0]))

    def test_extract_state_from_match(self):
        self.assertEqual("TX", extract_state_from_match(self.matches[0]))

    def test_get(self):
        # Match
        query = {'country' : 'US',
                 'state' : 'TX',
                 'city' : 'Austin',
                 'company_name' : 'Dell'
                 }
        response = get_matches(self.auth_token, confidence_code=5, **query)
        f = open("match_example_response.txt", "w")

        obj = json.loads(response)
        confidence_code = obj['MatchResponse']['MatchResponseDetail']['MatchCandidate'][0]['MatchQualityInformation']['ConfidenceCodeValue']
        print response
        f.write(response)
        f.close()

        self.assertTrue(response)
        self.assertEqual(7, confidence_code)


