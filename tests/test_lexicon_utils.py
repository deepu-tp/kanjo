from nose.tools import *

import kanjo.utils.lexicon_utils as lexicon_utils 
import unittest
import os


class TestLexiconsUtils(unittest.TestCase):

    def test_replace_slangs(self):
        text = lexicon_utils.replace_slangs('I g2g')
        assert_equal(text, 'I got to go')

    def test_emoticon_polarity(self):
        polarity = lexicon_utils.emoticon_polarity(':) :) :( :-(')
        assert_equal(polarity, 'Negative')

    def test_hashtag_polarity(self):
        polarity = lexicon_utils.hashtag_polarity(
                        'What a #swell day. It was #flawless')
        assert_equal(polarity, 'Positive')