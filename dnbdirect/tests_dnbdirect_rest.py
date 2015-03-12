import dnbdirect

from dnbdirect.rest import get_auth_token, get_dcp_premium, get_dcp_enhanced, get_commercial_credit_score, get_viability_rating, \
    get_viability_score, get_pbpre_enhanced, get_sers, get_fss, get_entity_match, get_triple_play, get_triple_play_composite_score

import sys
import unittest
import json
import os

class TestDnbDirect(unittest.TestCase):

    def setUp(self):
        self.token = get_auth_token(os.environ['API_USERNAME'], os.environ['API_PASSWORD'])

    #@unittest.skip("skipping")
    def testGetAuthToken(self):
        assert self.token

    #@unittest.skip("skipping")
    def testGetDCPPremium(self):
        duns = '177667227'
        try:
            dcp = get_dcp_premium(duns, self.token)
            print dcp
            assert dcp
        except Exception as e:
            print e
            self.fail("Couldn't load Detailed Company Profile for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetDCPEnhanced(self):
        duns = '177667227'
        try:
            dcp = get_dcp_enhanced(duns, self.token)
            print dcp
            assert dcp
        except Exception as e:
            print e
            self.fail("Couldn't load Detailed Company Profile for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetMarketingPrescreenScore(self):
        duns = '060704780'
        try:
            dcp = get_dcp_enhanced(duns, self.token)
            print dcp
            assert dcp
        except Exception as e:
            print e
            self.fail("Couldn't load Detailed Company Profile for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetCommercialCreditScore(self):
        duns = '060704780'
        try:
            [text, value] = get_commercial_credit_score(duns, self.token)
            print text
            print value
            assert text
            assert value
        except Exception as e:
            print e
            self.fail("Couldn't load Detailed Company Profile for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetViabilityRating(self):
        duns = '060704780'
        try:
            viab_rat = get_viability_rating(duns, self.token)
            print viab_rat
            assert viab_rat
        except Exception as e:
            self.fail("Couldn't load Viability Rating for duns #" + duns)

    #@unittest.skip("Skipping")
    def testGetViabilityScore(self):
        duns = '060704780'
        try:
            viab_score = get_viability_score(duns, self.token)
            assert viab_score
        except Exception as e:
            self.fail("Couldn't load Viability Score for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetPbpreEnhanced(self):
        duns = '060704780'
        try:
            pbpre = get_pbpre_enhanced(duns, self.token)
            assert pbpre
        except Exception as e:
            self.fail("Couldn't load PBPRE_ENH for duns #" + duns)

    #@unittest.skip("skipping")
    def testGetSERS(self):
        duns = '060704780'
        try:
            sers = get_sers(duns, self.token)
            assert sers
        except Exception as e:
            self.fail("Coudn't load SERS for duns # " + duns)

    def testGetFSS(self):
        duns = '060704780'
        fss = None
        try:
            fss = get_fss(duns, self.token)
        except Exception as e:
            print "Error: ", sys.exc_info()[0]
            self.fail("Coudn't load FSS for duns # " + duns)
        assert fss
        raw_score = fss[0]
        assert raw_score
        class_score = fss[1]
        assert class_score

    #@unittest.skip("skipping")
    def testMatch(self):
        matches = get_entity_match("Dell", self.token)
        assert matches

    #@unittest.skip("skipping")
    def testGetTriplePlay(self):
        duns = '060704780'
        triple_play = get_triple_play(duns, self.token)
        assert triple_play

    def testGetTriplePlayCompositeScore(self):
        duns = '060704780'
        score = get_triple_play_composite_score(duns, self.token)
        print "---- Score: " + str(score)
        assert score

if __name__ == "__main__":
    unittest.main()
