import kanjo.utils.lexicon_utils as lexicon_utils 
import numpy as np
import os
import pandas

from sklearn.externals import joblib

from kanjo.utils import import_from_string

def load_training_data(training_data):

    # Load data
    path = training_data['path']
    data = pandas.read_csv(path, encoding='utf-8')

    # Preprocessing
    if training_data.get('preprocess', False):
        for step in training_data['preprocessing']:
            if step.get('skip', False):
                continue
            method = import_from_string(step['name'])
            data = method(data, *step.get('args', []),
                          **step.get('kwargs', {}))

    return data


def transform_col_values(df, column_map, value_map):
    for column, new_column in column_map.iteritems():
        df[new_column] = df[column].apply(lambda x: value_map[x])
    return df


def remove_newline(df, columns):
    for column in columns:
        df[column] = df[column].apply(lambda x: x.replace('\n', ' '))
    return df


def remove_non_english(df, text_field):
    df = df[df[text_field].apply(lexicon_utils.is_english)]
    return df


def filter_row_values(df, column_values_map):
    for column, values in column_values_map.iteritems():
        df = df[df[column].isin(values)]
    return df


def unbias_row_values(df, column):
    grouped = df.groupby(column, as_index=False)
    _min_group = min(grouped.groups.iteritems(), key=lambda x: len(x[1]))
    
    min_count = len(_min_group[1])
    df = grouped.apply(lambda x: x[:min_count])
    return df


def grid_search_report(search):

    results = []
    parameters = []
    for score in search.grid_scores_:
        results.append({
            'std' : np.std(score.cv_validation_scores),
            'mean' : score.mean_validation_score,
        })
        parameters.append(score.parameters)
    
    grid = pandas.DataFrame(results)
    parameters = pandas.DataFrame(parameters)

    report = grid.merge(parameters, right_index=True, left_index=True)
    report = report.sort(['mean'], ascending=False)
    return report

def save_model(model, path):

    folder = os.path.dirname(path)
    for _file in os.listdir(folder):
        file_path = os.path.join(folder, _file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e

    joblib.dump(model, path)