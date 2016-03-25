# -*- coding: utf-8 -*-

import pytest
from simple_graph import SimpleGraph


@pytest.fixture()
def test_graph():
    test_dict = {
        1: {2: 3, 3: 5},
        2: {1: 3},
        3: {2: 7, 10: 8},
        10: {}
    }
    test_graph = SimpleGraph()
    test_graph._graph_content = test_dict
    return test_graph

@pytest.fixture()
def test_shortest_route():
    route_dict = {
        1: {2: 8, 3: 7},
        2: {10: 11},
        3: {2: 13, 10: 3, 5: 1},
        10: {},
        5: {}
    }
    test_route = SimpleGraph()
    test_route._graph_content = route_dict
    return test_route


def test_init():
    test_graph = SimpleGraph()
    assert test_graph._graph_content == {}


def test_nodes(test_graph):
    assert test_graph.nodes() == [1, 2, 3, 10]


def test_edges(test_graph):
    assert test_graph.edges() == [(1, [2, 3]), (2, [1]), (3, [2, 10]), (10, [])]


def test_add_node(test_graph):
    test_graph.add_node(4)
    assert test_graph._graph_content[4] == {}


def test_add_repeat_node(test_graph):
    with pytest.raises(ValueError):
        test_graph.add_node(3)


def test_add_edge_new_node(test_graph):
    test_graph.add_edge(4, 2, 3)
    assert test_graph._graph_content[4] == {2: 3}


def test_add_edge_existing_node(test_graph):
    test_graph.add_edge(10, 1, 5)
    assert test_graph._graph_content[10] == {1: 5}


def test_add_edge_overwrite_node(test_graph):
    test_graph.add_edge(1, 2, 11)
    assert test_graph._graph_content[1] == {2: 11, 3: 5}

def test_del_node(test_graph):
    test_graph.del_node(3)
    assert test_graph.edges() == [(1, [2]), (2, [1]), (10, [])]


def test_del_edge(test_graph):
    test_graph.del_edge(3, 2)
    assert test_graph._graph_content[3] == {10: 8}


def test_has_node_true(test_graph):
    assert test_graph.has_node(1) is True


def test_has_node_false(test_graph):
    assert test_graph.has_node(5) is False


def test_neighbors(test_graph):
    assert test_graph.neighbors(2) == [1]


def test_bad_neighbors(test_graph):
    with pytest.raises(ValueError):
        test_graph.neighbors(6)


def test_adjacent_true(test_graph):
    assert test_graph.adjacent(3, 2) is True


def test_adjacent_false(test_graph):
    assert test_graph.adjacent(2, 10) is False


def test_bad_adjacent(test_graph):
    with pytest.raises(ValueError):
        test_graph.adjacent(34, 56)


def test_dfs_cyclic(test_graph):
    assert test_graph.depth_first_traversal(1) == [1, 3, 10, 2]


def test_dfs_non_cyclic(test_graph):
    assert test_graph.depth_first_traversal(2) == [2, 1, 3, 10]


def test_bfs_cyclic(test_graph):
    assert test_graph.breadth_first_traversal(1) == [1, 2, 3, 10]


def test_bfs_non_cyclic(test_graph):
    assert test_graph.breadth_first_traversal(2) == [2, 1, 3, 10]


def test_dijkstra_route(test_shortest_route):
    assert test_shortest_route.dijkstra_route(1, 10) == [1, 3, 10]
