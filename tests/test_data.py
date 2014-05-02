from nose.tools import *

from kanjo.data import geo, lexicons
import unittest
import os

class TestGeoData(unittest.TestCase):

    def test_state_coordinates(self):
        assert_equal(type(geo.state_coordinates), list)


    def test_state_regions(self):
        assert_equal(type(geo.state_regions_divisions), dict)


class TestLexicons(unittest.TestCase):

    def test_afinn(self):
        assert_equal(type(lexicons.AFINN), list)


    def test_emoticons(self):
        assert_equal(type(lexicons.Emoticons), list)


    def test_nrc(self):
        assert_equal(type(lexicons.NRCHashtags), list)


    def test_slangs(self):
        assert_equal(type(lexicons.Slangs), list)


    def test_afinn_index(self):
        index = lexicons.AFINN_index
        query = index.query('Same Shit Different Day.')
        assert_equal(query, [('shit', -4)])


    def test_nrc_lkp(self):
        lkp = lexicons.NRCHashtags_lkp
        assert_equal(lkp['#highexpectations'], 0.478)

    def test_slangs_index(self):
        index = lexicons.Slangs_index
        query = index.query("I'll fix you l8r. g2g")
        assert_equal(query, [('l8r', 'later'), ('g2g', 'got to go')])