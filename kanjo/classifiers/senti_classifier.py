from __future__ import absolute_import
from senti_classifier import senti_classifier

def classify(text, verbose=False):

    polarity = 'Neutral'

    pos_score, neg_score = senti_classifier.polarity_scores([text])
    neg_score = -neg_score

    if pos_score + neg_score > 0:
        polarity = "Positive"

    elif pos_score + neg_score < 0:
        polarity = "Negative"


    if verbose:
        return {

            'pos_score' : pos_score,
            'neg_score' : neg_score,
            'polarity' : polarity,
            'total_score' : pos_score + neg_score 

        }

    return polarity