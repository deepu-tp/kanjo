import json
import jsonrpclib
from pprint import pprint

class StanfordNLPSentiment:
    _instance = None

    POLARITY_MAP = {
        'Very positive' : 4,
        'Positive' : 3,
        'Neutral' : 2,
        'Negative' : 1,
        'Very negative' : 0
    }

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(StanfordNLPSentiment, cls).__new__(cls)
        return cls._instance


    def __init__(self, url):
        self.server = jsonrpclib.Server(url)


    def classify(self, text, verbose=False):

        polarity = self.server.parse(text)
        result = {}
        result['polarity_score'] = self.POLARITY_MAP[polarity]
        result['polarity'] = polarity

        if verbose:
            return result

        return result['polarity']