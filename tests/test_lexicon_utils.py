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

    def test_afinn_polarity(self):
        polarity = lexicon_utils.afinn_polarity(
                        'what a wonderful day It was flawless')
        assert_equal(polarity, 'Positive')

    def test_is_english(self):
        is_english = lexicon_utils.is_english("I hope this is in english")
        assert_equal(is_english, True)

        is_english = lexicon_utils.is_english(("oi muito bem vinda ao meu "
                                               "twitter sempre dou followback"
                                               " pelo meu perfil profissional"
                                               "permaneca por aqui certo"
                                               " abrass"))
        assert_equal(is_english, False)