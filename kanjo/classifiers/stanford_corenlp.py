import json
import jsonrpclib
from pprint import pprint

class StanfordNLPSentiment:
    _instance = None


    def __new__(cls):
        if not cls._instance:
            cls._instance = super(StanfordNLPSentiment, cls).__new__(cls)
        return cls._instance


    def __init__(self, url):
        self.server = jsonrpclib.Server(url)


    def classify(self, text):
        return self.server.parse(text)