from nose.tools import *

from kanjo.classifiers.stanford_corenlp import StanfordNLPSentiment
import unittest
import os


class TestStanfordNLPSentiment(unittest.TestCase):

    def setUp(self):
        self.client = StanfordNLPSentiment('http://localhost:8080')

    def tearDown(self):
        pass

    def test_classify(self):
        result = self.client.classify("What a wonderful test!")
        assert_equal(result, 'Very positive')
