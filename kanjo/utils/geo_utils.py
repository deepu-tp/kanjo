from kanjo.data import geo
import math


def _dist(x1, y1, x2, y2):
    x_dist = math.pow((x1 - x2), 2.0)
    y_dist = math.pow((y1 - y2), 2.0)        
    return math.sqrt((x_dist + y_dist))


def get_state_containing_point(lat, lng):
    dists = map(lambda state: 
                {'delta' : _dist(state['longitude'], state['latitude'],
                                 lng, lat),
                 'code' : state['state']}, geo.state_coordinates)

    state = min(dists, key=lambda x: x['delta'])
    return state['code']