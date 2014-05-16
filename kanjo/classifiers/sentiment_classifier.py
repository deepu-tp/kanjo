from kanjo.classifiers.trained_classifier import TrainedClassifier

class SentimentClassifier(TrainedClassifier):
    _instance = None

    POLARITY_SCORE_MAP = {
        0 : 'Negative',
        1 : 'Positive'
    }