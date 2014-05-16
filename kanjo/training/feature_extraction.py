import pandas

from kanjo.classifiers.stanford_corenlp import StanfordNLPSentiment
from kanjo.classifiers.sentiment140 import Sentiment140
from kanjo.twitter.utils import preprocess_tweet_text
from kanjo.utils.lexicon_utils import (
    replace_slangs,
    emoticon_polarity,
    hashtag_polarity,
    afinn_polarity
)

def extract_features(df, stanford_corenlp_url, sentiment140_appid,
                     text_field):

    corenlp_client = StanfordNLPSentiment(stanford_corenlp_url)
    sentiment140_client = Sentiment140(sentiment140_appid)

    df['processed_text'] = df[text_field].apply(preprocess_tweet_text)

    df = df.merge(df['processed_text'].apply(
                lambda x: pandas.Series(afinn_polarity(x, verbose=True)
                          ).rename(index=lambda c: 'afinn_%s' % c)
             ), left_index=True, right_index=True)

    df = df.merge(df[text_field].apply(
                lambda x: pandas.Series(emoticon_polarity(x, verbose=True)
                          ).rename(index=lambda c: 'emoticon_%s' % c)
             ), left_index=True, right_index=True)

    df = df.merge(df[text_field].apply(
                lambda x: pandas.Series(hashtag_polarity(x, verbose=True)
                          ).rename(index=lambda c: 'hashtag_%s' % c)
             ), left_index=True, right_index=True)


    df = df.merge(df['processed_text'].apply(
                lambda x: pandas.Series(
                            corenlp_client.classify(x, verbose=True)
                          ).rename(index=lambda c: 'stanford_corenlp_%s' % c)
             ), left_index=True, right_index=True)

    df['id'] = df.index.values
    _data = df[[text_field, 'id']]
    _data = _data.rename(columns = {text_field : 'text'}).to_dict('records')
    results = pandas.DataFrame(sentiment140_client.bulk_classify(_data,
                               verbose=True))
    results = results.drop('text', axis=1)
    results = results.rename(columns=lambda x: 
                                x != 'id' and 'sentiment140_%s' % x or x)

    df = df.merge(results, on='id')
    df = df.drop('id', axis=1)

    return df