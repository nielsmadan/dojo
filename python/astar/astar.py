from collections import defaultdict
from Queue import PriorityQueue, Empty
from math import sqrt

import sys

infinity = sys.maxint

GRAPH_STRING = [
    "---------------------",
    "------------------T--",
    "----XXXXXXXXXX-------",
    "-------------X-------",
    "-------------X-------",
    "------S------X-------",
    "-------------X-------",
    "-------------X-------",
    "---------------------",
]


def get_neighbors(node_list, y, x):
    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((y + i) >= 0 and (y + i) < len(node_list) and
                    (x + j) >= 0 and (x + j) < len(node_list[0]) and
                    not (i == 0 and j == 0)):
                result.append(node_list[y + i][x + j])

    return filter(lambda x: x is not None, result)


class Graph(object):
    def __init__(self, node_dict=None, start=None, target=None):
        if node_dict is not None:
            self.node_dict = node_dict
            self.start_node = start
            self.target_node = target
        else:
            self.node_dict = defaultdict(list)
            self.start_node = None
            self.target_node = None

    def add_node(self, node, neighbors):
        self.node_dict[node].extend(neighbors)

    def get_neighbors(self, node):
        return self.node_dict[node]

    def __str__(self):
        return '\n'.join(["%s: %s" % (key, val) for key, val in self.node_dict.iteritems()])

    @staticmethod
    def find_node(node_list, string_repr, search_type):
        for y, node_row in enumerate(string_repr):
            for x, node in enumerate(node_row):
                if string_repr[y][x] == search_type:
                    return node_list[y][x]

        assert False

    @staticmethod
    def from_string(string_graph):
        def create_node(c, x, y):
            if c is not "X":
                return Node(x, y)

        node_list = []

        for y, row in enumerate(string_graph):
            node_row = []
            for x, node_string in enumerate(row):
                node_row.append(create_node(node_string, x, y))

            node_list.append(node_row)

        start_node = Graph.find_node(node_list, string_graph, 'S')
        target_node = Graph.find_node(node_list, string_graph, 'T')

        node_dict = defaultdict(list)
        for y, row in enumerate(node_list):
            for x, node in enumerate(row):
                if node is not None:
                    node_dict[node] = get_neighbors(node_list, y, x)

        return Graph(node_dict, start_node, target_node)


class Node(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return "Y: %s, X: %s" % (self.y, self.x)


def find_target_node(graph):
    return next(node for node in graph.node_dict.keys() if node.is_target)


def find_ancestors(ancestors_dict, leaf_node, root_node):
    current_node = leaf_node
    result_list = [current_node]

    while current_node != root_node:
        current_node = ancestors_dict[current_node]
        result_list.append(current_node)

    assert result_list[-1] == root_node

    return result_list


def euclidean_distance(node1, node2):
    return sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def astar_cost_function(current_distance, current_node, target_node):
    return current_distance + euclidean_distance(current_node, target_node)


def dijkstra_cost_function(current_distance, current_node, target_node):
    return current_distance


class PathFinder(object):
    def __init__(self, cost_function):
        self.cost_function = cost_function
        self.nodes_visited = 0
        self.nodes_expanded = 0

    def __call__(self, graph, start_node, target_node):
        frontier = PriorityQueue()

        current_node = start_node
        distance_dict = defaultdict(lambda: infinity)
        distance_dict[current_node] = 0
        ancestors_dict = {}
        visited_set = set()

        while True:
            neighbors = graph.get_neighbors(current_node)

            current_distance = distance_dict[current_node]

            for neighbor in neighbors:
                if neighbor not in visited_set and (current_distance + 1) < distance_dict[neighbor]:
                    distance_dict[neighbor] = current_distance + 1
                    ancestors_dict[neighbor] = current_node
                    frontier.put((self.cost_function(distance_dict[neighbor], neighbor, target_node), neighbor))
                    self.nodes_expanded += 1

            visited_set.add(current_node)
            self.nodes_visited += 1

            if current_node == target_node:
                return list(reversed(find_ancestors(ancestors_dict, current_node, start_node)))
            else:
                try:
                    current_node = frontier.get_nowait()[1]
                except Empty:
                    break
