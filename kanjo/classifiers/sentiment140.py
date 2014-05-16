from __future__ import absolute_import
from sentiment140.api import Sentiment140API


class Sentiment140:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Sentiment140, cls).__new__(cls)
        return cls._instance


    def __init__(self, appid):
        self.api = Sentiment140API(appid)


    def _get_polarity_name(self, polarity_score):
        if polarity_score == 0:
            return 'Negative'
        elif polarity_score == 2:
            return 'Neutral'
        else:
            return 'Positive'


    def classify(self, text, verbose=False):

        result = self.api.classify(text)
        result['polarity_score'] = result['polarity']
        result['polarity'] = self._get_polarity_name(result['polarity'])

        if verbose:
            return result

        return result['polarity']


    def bulk_classify(self, data, verbose=False):

        results = self.api.bulk_classify_json(data)
        for result in results:
            result['polarity_score'] = result['polarity']
            result['polarity'] = self._get_polarity_name(result['polarity'])

        if verbose:
            return results

        return map(lambda x: x['polarity'], results)