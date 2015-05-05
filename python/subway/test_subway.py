import subway
from nose.tools import eq_

boston = subway.subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan'
)

def test_subway_single():
    simple = subway.subway(blue="stationA stationB")

    eq_(simple["stationA"], { "stationB": "blue" })
    eq_(simple["stationB"], { "stationA": "blue" })

def test_subway_crossing():
    crossing = subway.subway(blue="stationA stationB", orange="stationC stationA stationD")
    eq_(crossing["stationA"], { "stationB": "blue", "stationC": "orange", "stationD": "orange" })

def test_ride_simple():
    simple_ride = subway.ride("stationA", "stationB", subway.subway(blue="stationA stationB"))
    eq_(simple_ride, ["stationA", "blue", "stationB"])

def test_ride_slightly_less_simple():
    simple_ride = subway.ride("stationA", "stationC",
                              subway.subway(blue="stationA stationB stationC"))
    eq_(simple_ride, ["stationA", "blue", "stationB", "blue", "stationC"])

def test_ride_mit_government():
    eq_(subway.ride('mit', 'government', boston), [ 'mit', 'red', 'charles', 'red', 'park', 'green', 'government'])

def test_ride_mattapan_foresthills():
    eq_(subway.ride('mattapan', 'foresthills', boston), [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills'])

def test_ride_newton_alewife():
    eq_(subway.ride('newton', 'alewife', boston), [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife'])
