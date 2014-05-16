from kanjo.utils.geo_utils import get_state_containing_point
from kanjo.data import geo
import kanjo.utils.lexicon_utils as lexicon_utils
import translitcodec
import re

def enrich_geo(tweet):

    location = {'world' : 'WW'}

    place = tweet.get('place', {})

    country = ''
    if 'country_code' in place:
        country = place['country_code']
        location['country'] = country

    try:
        coords = tweet['coordinates']['coordinates']
    except (KeyError, TypeError):
        coords = None

    state = ''
    if country == 'US':
        if coords:
            lat = coords[1]
            lng = coords[0]
            state = get_state_containing_point(lat, lng)
            location['state'] = state
            
        elif (place and place['bounding_box']['coordinates'][0]):
            bbox = place['bounding_box']['coordinates'][0]
            avgcoord = map(lambda x: x * 1.0 / len(bbox),
                           reduce(lambda x, y: ((y[0] + x[0]),
                                                 (y[1] + x[1])),
                                   bbox, (0, 0)))

            lat = avgcoord[1]
            lng = avgcoord[0]
            state = get_state_containing_point(lat, lng)
            location['state'] = state
            location[place['place_type']] = place['name']

    try:
        region = geo.state_regions_divisions[state]
    except KeyError:
        pass
    else:
        location['division'] = region['Division']
        location['region'] = region['Region']
    
    return location


def preprocess_tweet_text(text):
    #Convert to lower case
    text = text.lower()

    # Replace newline characters with space
    text = text.replace('\n', ' ')

    # Try to replace 
    text = text.encode('translit/long').encode('ascii', 'ignore')

    #substitute the slangs
    text = lexicon_utils.replace_slangs(text)

    #Remove www.* or https?://* 
    text = re.sub('((www\.[\s]+)|(https?://[^\s]+))','',text)

    #Remove @username 
    text = re.sub('(rt)? @[^\s]+','',text)

    #Remove additional white spaces
    text = re.sub('[\s]+', ' ', text)

    #Replace #word with word
    text = re.sub(r'#([^\s]+)', r'\1', text)

    #Remove the numbers
    text = re.sub('[0-9]*','',text)

    #Remove Punctuations
    text = re.sub(r'[^\w\s]','',text)

    #trim
    text = text.strip('\'"')

    #trim
    text = text.strip()
 
    return text
