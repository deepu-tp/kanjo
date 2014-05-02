from nose.tools import *

from kanjo.classifiers.sentiment140 import Sentiment140
import unittest
import os


class TestSentiment140(unittest.TestCase):

    def setUp(self):
        self.api = Sentiment140('')

    def test_classify(self):
        result = self.api.classify("What a wonderful test!")
        assert_equal(result, 'Positive')

    def test_bulk_classify(self):
        result = self.api.bulk_classify([{'text' : "What a wonderful test!"}])
        assert_equal(result, ['Positive'])