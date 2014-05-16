import importlib
import numpy as np
import os
import pandas
import pydot

from kanjo.training.feature_extraction import extract_features
from kanjo.training.utils import (
    load_training_data,
    grid_search_report,
    save_model
)
from kanjo.utils import import_from_string

from sklearn.cross_validation import ShuffleSplit
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV


def train(config):
    settings = config['settings']

    training_data = settings['training_data']
    data = load_training_data(training_data)
    data.to_csv(os.path.join(config['data_dir'], 'processed_data.csv'),
                encoding='utf-8', index=False)

    # Extract features
    if training_data.get('extract_features', False):
        data = extract_features(data, settings['stanford_corenlp_url'],
                                settings['sentiment140_appid'],
                                training_data['text_field'])
        data.to_csv(os.path.join(config['data_dir'], 'training_data.csv'),
                    encoding='utf-8', index=False)

    features = data.filter(items=training_data['features'], axis=1)
    label = data[training_data['label']]

    classifier = ExtraTreesClassifier(n_estimators=30)

    cv_kwargs = settings['cross_validation']['kwargs']
    cross_validation = ShuffleSplit(len(label), **cv_kwargs)

    gs_args = settings['grid_search']['args']
    gs_kwargs = settings['grid_search']['kwargs']

    gs = GridSearchCV(classifier, *[gs_args], cv=cross_validation,
                      **gs_kwargs)

    gs.fit(features, label)

    report = grid_search_report(gs)
    print report

    model = gs.best_estimator_
    print model

    model._features = training_data['features']

    save_model(model, os.path.join(config['model_save_dir'], 'model'))