from nose.tools import *

from kanjo.classifiers.sentiment_classifier import SentimentClassifier
import unittest
import os


class TestSentimentClassifier(unittest.TestCase):

    def setUp(self):
        self.clsf = SentimentClassifier(
            'data/sentiment_classifier/sentiment_classifier_v0.1/model/model'
            )

    def test_classify(self):

        result = self.clsf.classify({

                    'emoticon_pos_score' : 5,
                    'emoticon_neg_score' : 0,
                    'hashtag_pos_score' : 3,
                    'hashtag_neg_score' : 0,
                    'afinn_pos_score' : 5,
                    'afinn_neg_score' : 0,
                    'stanford_corenlp_polarity_score' : 3,
                    'sentiment140_polarity_score' : 4
                })

        assert_equal(result, 'Positive')