from nose.tools import *

import kanjo.twitter.utils as twitter_utils 
import unittest
import os


class TestTwitterUtils(unittest.TestCase):


    def test_get_state_containing_point(self):
        pass


    def test_preprocess_tweet_text(self):
        text = twitter_utils.preprocess_tweet_text('I g2g now.')
        assert_equal(text, 'i got to go now')