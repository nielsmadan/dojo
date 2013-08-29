import astar
from nose.tools import eq_, ok_
from math import sqrt

FULL_TEST_GRAPH = (
    "---------------------",
    "------------------T--",
    "----XXXXXXXXXX-------",
    "-------------X-------",
    "-------------X-------",
    "------S------X-------",
    "-------------X-------",
    "-------------X-------",
    "---------------------",
)


def test_find_node_row():
    node_a = astar.Node()
    node_b = astar.Node()

    result = astar.Graph.find_node([[node_a, node_b]], ["-S"], 'S')

    eq_(result, node_b)


def test_find_node_column():
    node_a = astar.Node()
    node_b = astar.Node()

    result = astar.Graph.find_node([[node_a], [node_b]], ["-", "S"], 'S')

    eq_(result, node_b)


def test_get_graph():
    graph = astar.Graph.from_string(["T",
                                     "S"])

    node_keys = graph.node_dict.keys()
    eq_(graph.node_dict[node_keys[0]], [node_keys[1]])
    eq_(graph.node_dict[node_keys[1]], [node_keys[0]])


def test_get_neighbors_one_row_neighbor():
    node_a = astar.Node()
    node_b = astar.Node()

    neighbor_list = astar.get_neighbors([[node_a, node_b]], 0, 0)
    eq_(neighbor_list, [node_b])

    neighbor_list = astar.get_neighbors([[node_a, node_b]], 0, 1)
    eq_(neighbor_list, [node_a])


def test_get_neighbors_one_column_neighbor():
    node_a = astar.Node()
    node_b = astar.Node()

    neighbor_list = astar.get_neighbors([[node_a], [node_b]], 0, 0)
    eq_(neighbor_list, [node_b])

    neighbor_list = astar.get_neighbors([[node_a], [node_b]], 1, 0)
    eq_(neighbor_list, [node_a])


def test_get_neighbors_none_neighbor():
    node_a = astar.Node()

    neighbor_list = astar.get_neighbors([[node_a], [None]], 0, 0)
    eq_(neighbor_list, [])


def test_find_ancestors():
    input_dict = {
        'b': 'a',
        'c': 'b',
    }

    result = astar.find_ancestors(input_dict, 'c', 'a')

    eq_(result, ['c', 'b', 'a'])


def test_find_ancestors_two_levels():
    input_dict = {
        'b': 'a',
        'c': 'b',
        'd': 'c',
    }

    result = astar.find_ancestors(input_dict, 'd', 'a')

    eq_(result, ['d', 'c', 'b', 'a'])


def test_dijkstra_two_node_graph():
    graph = astar.Graph.from_string("ST")

    result = astar.PathFinder(astar.dijkstra_cost_function)(graph, graph.start_node, graph.target_node)

    eq_(result, [graph.start_node, graph.target_node])


def test_dijkstra_three_node_graph():
    start_node = astar.Node()
    target_node = astar.Node()
    middle_node = astar.Node()

    graph = astar.Graph()

    graph.add_node(start_node, [middle_node])
    graph.add_node(middle_node, [start_node, target_node])
    graph.add_node(target_node, [middle_node])

    result = astar.PathFinder(astar.dijkstra_cost_function)(graph, start_node, target_node)

    eq_(result, [start_node, middle_node, target_node])


def test_dijkstra_impossible():
    start_node = astar.Node()
    target_node = astar.Node()
    middle_node = astar.Node()

    graph = astar.Graph()

    graph.add_node(start_node, [middle_node])
    graph.add_node(middle_node, [start_node])
    graph.add_node(target_node, [])

    result = astar.PathFinder(astar.dijkstra_cost_function)(graph, start_node, target_node)

    eq_(result, None)


def test_dijkstra_complex_graph():
    graph = astar.Graph.from_string(FULL_TEST_GRAPH)

    path_finder = astar.PathFinder(astar.dijkstra_cost_function)
    result = path_finder(graph, graph.start_node, graph.target_node)

    eq_(result[0], graph.start_node)
    eq_(result[-1], graph.target_node)
#
#     print "DIJKSTRA VISITED: %s" % path_finder.nodes_visited
#     print "DIJKSTRA EXPANDED: %s" % path_finder.nodes_expanded


def test_astar_complex_graph():
    graph = astar.Graph.from_string(FULL_TEST_GRAPH)

    path_finder = astar.PathFinder(astar.astar_cost_function)
    result = path_finder(graph, graph.start_node, graph.target_node)

    eq_(result[0], graph.start_node)
    eq_(result[-1], graph.target_node)
#
#     print "ASTAR VISITED: %s" % path_finder.nodes_visited
#     print "ASTAR EXPANDED: %s" % path_finder.nodes_expanded


def test_euclidean_distance():
    result = astar.euclidean_distance(astar.Node(1, 1), astar.Node(2, 2))

    eq_(result, sqrt(2))
