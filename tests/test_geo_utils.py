from nose.tools import *

import kanjo.utils.geo_utils as geo_utils 
import unittest
import os


class TestGeoUtils(unittest.TestCase):

    def test_get_state_containing_point(self):
        lat = 14.2417
        lng = -170.7197
        state = geo_utils.get_state_containing_point(lat, lng)
        assert_equal(state, 'AS')