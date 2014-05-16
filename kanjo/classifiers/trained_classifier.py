from sklearn.externals import joblib

class TrainedClassifier:
    _instance = None

    POLARITY_SCORE_MAP = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BaseClassifier, cls).__new__(cls)
        return cls._instance


    def __init__(self, path):
        self.model = joblib.load(path)


    def _feature_vector(self, data):
        return [data[k] for k in self.model._features]


    def classify(self, data, verbose=False):

        features = self._feature_vector(data)
        polarity_score = self.model.predict(features)[0]

        result = {}
        result['polarity'] = self.POLARITY_SCORE_MAP[polarity_score]
        result['polarity_score'] = polarity_score

        if verbose:
            return result

        return result['polarity']