import pprint
from collections import defaultdict

def subway(**lines):
    """Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}"""

    network = defaultdict(dict)

    for line, stations_string in lines.iteritems():
        stations = stations_string.split()

        # for (station, neighbor1, neighbor2) in zip(stations, [None] + stations[1:], stations[:-1] + [None]):
        #     if neighbor1 is not None:
        #         network[station][neighbor1] = line
        #     if neighbor2 is not None:
        #         network[station][neighbor2] = line

        for i, station in enumerate(stations):
            if i > 0:
                neighbor = stations[i - 1]
                network[station][neighbor] = line
            if i < len(stations) - 1:
                neighbor = stations[i + 1]
                network[station][neighbor] = line

    return network

def ride(here, there, system):
    "Return a path on the subway system from here to there."
    neighbor_path = [(neighbor, [here, line]) for (neighbor, line) in system[here].iteritems()]
    visited = set([here])

    while len(neighbor_path) > 0:
        (neighbor, path) = neighbor_path.pop(0)

        if neighbor == there:
            return path + [there]

        visited.add(neighbor)
        neighbor_path.extend([(new_neighbor, path + [neighbor, line])
                              for (new_neighbor, line) in system[neighbor].iteritems()
                              if new_neighbor not in visited])


def longest_ride(system):
    """"Return the longest possible 'shortest path' ride between any two stops in the system."""
    pass
