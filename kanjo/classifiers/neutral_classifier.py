from kanjo.classifiers.trained_classifier import TrainedClassifier

class NeutralClassifier(TrainedClassifier):
    _instance = None

    POLARITY_SCORE_MAP = {
        0 : 'Not Neutral',
        1 : 'Neutral'
    }