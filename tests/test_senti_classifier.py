from nose.tools import *

from kanjo.classifiers.senti_classifier import classify
import unittest
import os


class TestSentiClassifier(unittest.TestCase):

    def test_classify(self):
        result = classify("What a wonderful test!")
        assert_equal(result, 'Positive')
