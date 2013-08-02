from collections import defaultdict


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


class Graph(object):
    def __init__(self, node_dict):
        self.node_dict = node_dict

    @staticmethod
    def from_string(string_graph):
        def get_node(c):
            if c is not "X":
                return Node(c == 'S', c == 'T')

        def get_neighbors(node_list, y, x):
            return [node_list[y + i][x + j] for i in range(-1, 2)
                                            for j in range(-1, 2)
                                                if (y + i) >= 0 and
                                                   (y + i) < len(node_list) and
                                                   (x + i) >= 0 and
                                                   (x + i) < len(node_list[0]) and
                                                   (i != 0 and j != 0)]

        node_list = [[Node(get_node(c)) for c in row] for row in string_graph]
        node_dict = {}
        for y, row in enumerate(node_list):
            for x, node in enumerate(row):
                if node is not None:
                    node_dict[node] = get_neighbors(node_list, y, x)

        return Graph(node_dict)


class Node(object):
    def __init__(self, start=False, target=False):
        self.is_start = start
        self.is_target = target


def find_start_node(graph):
    return next(node for node in graph.node_dict.keys() if node.is_start)


def find_target_node(graph):
    return next(node for node in graph.node_dict.keys() if node.is_target)


# def dijkstra(graph):
#     graph = assign_initial_distance(graph)
#     # graph = mark_initial_graph_unvisited(graph)
#
#     start_node = find_start(graph)
#     target_node = find_target(graph)
#
#     current_node = start_node
#     visited_nodes = []
#
#     while current_node is not None:
#         graph = calculate_neighbor_distances(current_node, graph, visited_nodes)
#
#         visited_nodes = mark_as_visited(current_node, visited_nodes)
#
#         if is_visited(target_node, unvisited_nodes):
#             return
#
#         current_node = find_smallest_distance_node(current_node, visited, graph)
