from nose.tools import *

from kanjo.classifiers.neutral_classifier import NeutralClassifier
import unittest
import os


class TestNeutralClassifier(unittest.TestCase):

    def setUp(self):
        self.clsf = NeutralClassifier(
            'data/neutral_classifier/neutral_classifier_v0.1/model/model'
            )

    def test_classify(self):

        result = self.clsf.classify({'afinn_polarity_score' : -10,
                                'stanford_corenlp_polarity_score' : 2,
                                'sentiment140_polarity_score' : 0})

        assert_equal(result, 'Not Neutral')