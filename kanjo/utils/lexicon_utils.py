from kanjo.data import lexicons
import translitcodec
import re


def replace_slangs(text):
    index = lexicons.Slangs_index
    query = index.query(text)

    words = list(enumerate(text.split(' ')))
    for matchl in query:
        for i, word in words:
            if matchl[0] == word.lower():
                words[i] = (i, matchl[1])

    return (' '.join([x[1] for x in words]))


def emoticon_polarity(text, verbose=False):
    text = text.encode('translit/long').encode('ascii', 'ignore')
    emoticons = lexicons.Emoticons

    useful = "F"
    polarity = 0
    emot_details = {}

    scores = filter(None, map(lambda x: x[0] in text.split() and x or None,
                              emoticons))

    polarity = 'Neutral'
    pos_score = 0
    neg_score = 0
    for emoticon, score in scores:
        score = int(score)
        if score > 0:
            pos_score += score
        else:
            neg_score += score

    if pos_score + neg_score > 0:
        polarity = "Positive"

    elif pos_score + neg_score < 0:
        polarity = "Negative"

    if verbose:
        return {
            'matches' : scores,
            'pos_score' : pos_score,
            'neg_score' : neg_score,
            'polarity_score' : pos_score + neg_score,
            'polarity' : polarity
        }

    return polarity


hastag_re = re.compile(r'(#[^\s]+)')
def hashtag_polarity(text, verbose=False):
    tags = hastag_re.findall(text)
    tag_lkp = lexicons.NRCHashtags_lkp

    matches = []
    pos_score = 0
    neg_score = 0
    polarity = 'Neutral'
    for tag in tags:
        try:
            score = tag_lkp[tag]
        except KeyError:
            continue

        else:
            matches.append((tag, score))
            if int(score) > 0:
                pos_score += score

            else:
                neg_score += score

    if pos_score + neg_score > 0:
        polarity = "Positive"

    elif pos_score + neg_score < 0:
        polarity = "Negative"

    if verbose:
        return {
            'matches' : matches,
            'pos_score' : pos_score,
            'neg_score' : neg_score,
            'polarity_score' : pos_score + neg_score,
            'polarity' : polarity
        }
    return polarity


def afinn_polarity(text, verbose=False):
    index = lexicons.AFINN_index
    query = index.query(text)

    words = list(text.split(' '))

    matches = []
    for match in query:
        if match[0] in words:
            matches.append(match)

    polarity = 'Neutral'
    pos_score = 0
    neg_score = 0
    for match, score in matches:
        if score > 0:
            pos_score += score
        else:
            neg_score += score

    if pos_score + neg_score > 0:
        polarity = "Positive"

    elif pos_score + neg_score < 0:
        polarity = "Negative"

    if verbose:
        return {
            'matches' : matches,
            'pos_score' : pos_score,
            'neg_score' : neg_score,
            'polarity_score' : pos_score + neg_score,
            'polarity' : polarity
        }

    return polarity


def is_english(text):
    lkp = lexicons.english_words_lkp
    words = text.lower().split(' ')

    english_words = 0
    for word in words:
        if word in lkp:
            english_words += 1

    if (english_words * 1.0 / len(words)) > 0.5:
        return True

    return False