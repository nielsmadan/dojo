import astar
from nose.tools import eq_, ok_

FULL_TEST_GRAPH = (
    "---------------------"
    "------------------T--"
    "----XXXXXXXXXX-------"
    "-------------X-------"
    "-------------X-------"
    "------S------X-------"
    "-------------X-------"
    "-------------X-------"
    "---------------------"
)


def test_find_start_single_node():
    graph = astar.Graph.from_string(["S"])
    ok_(astar.find_start_node(graph).is_start)


def test_find_start_single_row():
    graph = astar.Graph.from_string(["---S---"])
    ok_(astar.find_start_node(graph).is_start)


def test_find_start_multiple_row():
    graph = astar.Graph.from_string(["------", "---S---", "------"])
    ok_(astar.find_start_node(graph).is_start)


def test_find_target_single_node():
    graph = astar.Graph.from_string(["T"])
    ok_(astar.find_target_node(graph).is_target)


def test_find_target_single_row():
    graph = astar.Graph.from_string(["---T---"])
    ok_(astar.find_target_node(graph).is_target)


def test_find_target_multiple_row():
    graph = astar.Graph.from_string(["------", "---T---", "------"])
    ok_(astar.find_target_node(graph).is_target)


def test_get_graph():
    graph = astar.Graph.from_string(["-", "-"])

    node_keys = graph.node_dict.keys()
    eq_(graph.node_dict[node_keys[0]], [node_keys[1]])
    eq_(graph.node_dict[node_keys[1]], [node_keys[0]])
