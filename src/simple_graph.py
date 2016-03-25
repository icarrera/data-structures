# -*- coding: utf-8 *-*
from stack import Stack
from queue import Queue
import time


class SimpleGraph(object):
    """Python implementation of the simple graph structure."""

    def __init__(self):
        """SimpleGraph constructor."""
        self._graph_content = {}

    def nodes(self):
        """Return a list of the nodes."""
        return list(self._graph_content)

    def edges(self):
        """Return a list of nodes and their edges."""
        rtn_list = []
        # go through each node and its lists of paths.
        for key, nodes in self._graph_content.items():
            path_keys = []
            # for each path append the key to path_keys
            path_keys += nodes.keys()
            rtn_list.append((key, path_keys))
        return rtn_list


    def add_node(self, val):
        """Add a new node to the graph."""
        if self.has_node(val):
            raise ValueError
        self._graph_content[val] = {}

    def add_edge(self, node1, node2, weight):
        """Add a new edge to the graph connecting node1 to node2.

        Checks if they exist and adds them if they do not.
        """
        if not self.has_node(node1):
            self.add_node(node1)
        if not self.has_node(node2):
            self.add_node(node2)
            # if edge already exists, update weight
        self._graph_content[node1][node2] = weight

    def del_node(self, rem_node):
        """Remove the node from the graph if it exists. Error on Fail."""
        try:
            for key in self._graph_content:
                if self.adjacent(key, rem_node):
                    self.del_edge(key, rem_node)
            del self._graph_content[rem_node]
        except (KeyError, ValueError):
            raise ValueError

    def has_node(self, node):
        """True/False if the graph has node."""
        return node in self._graph_content

    def del_edge(self, node1, node2):
        """Remove the edge connected node1 to node2. Error on Fail."""
        if node2 in self._graph_content[node1].keys():
            del self._graph_content[node1][node2]

    def neighbors(self, node):
        """Return a list of all nodes with edges connected to node(param)."""
        if self.has_node(node):
            # go through each node and its lists of paths.
            return list(self._graph_content[node])
        raise ValueError

    def adjacent(self, node1, node2):
        """Return True or False if two nodes have a connection."""
        if self.has_node(node1) and self.has_node(node2):
            return (node2 in self.neighbors(node1))
        raise ValueError

    def depth_first_traversal(self, start):
        """Return the full visited path of a depth first traversal."""
        if not self.has_node(start):
            raise ValueError
        depth_stack = Stack()
        visited = []
        depth_stack.push(start)
        while depth_stack.size() > 0:
            checker = depth_stack.pop()
            if checker not in set(visited):
                visited.append(checker)
                for key in self._graph_content[checker].keys():
                    depth_stack.push(key)
        return visited

    def breadth_first_traversal(self, start):
        """Return the full visited path of a breadth first traversal."""
        if not self.has_node(start):
            raise ValueError
        breadth_queue = Queue()
        visited = []
        breadth_queue.enqueue(start)
        while breadth_queue.size() > 0:
            checker = breadth_queue.dequeue()
            if checker not in set(visited):
                visited.append(checker)
                for key in self._graph_content[checker].keys():
                    breadth_queue.enqueue(key)
        return visited

    def dijkstra_route(self, start, end):
        """Test shortest route between two nodes using Dijkstra's algorithm."""
        inf = float('inf')
        nodes_dict = {}
        unvisited = {}
        for key in self._graph_content:
            nodes_dict[key] = [inf, None]
        unvisited = nodes_dict.copy()
        unvisited[start] = [0, None]
        while unvisited:
            current = {}
            distance = list(unvisited.values())
            distance.sort()
            shortest = distance[0][0]
            for key in unvisited:
                if unvisited[key][0] == shortest:
                    current = {key: shortest}
                    del unvisited[key]
                    break
            cur_key = list(current)[0]
            for neighbor in self.neighbors(cur_key):
                distance = (current[cur_key] +
                            self._graph_content[cur_key][neighbor])
                if distance < unvisited[neighbor][0]:
                    unvisited[neighbor][0] = distance
                    unvisited[neighbor][1] = cur_key
                    nodes_dict[neighbor][1] = cur_key
        full_path = []
        prev_node = end
        while nodes_dict[prev_node][1]:
            full_path.append(prev_node)
            prev_node = nodes_dict[prev_node][1]
        full_path.append(start)
        return full_path[::-1]


if __name__ == '__main__':
    basic_graph = SimpleGraph()
    basic_graph._graph_content = {
        3: ['7', 5],
        '7': ['11', 5],
        '11': [],
        5: [10],
        10: ['7'],
    }

    print(u"Made Graph:{}".format(basic_graph.edges()))
    start1 = time.time()
    basic_graph.depth_first_traversal(3)
    end1 = time.time()
    print(u"Depth First Travel (from 3):")
    print(basic_graph.depth_first_traversal(3))
    print(u"Took {} seconds".format(end1-start1))

    start2 = time.time()
    basic_graph.breadth_first_traversal(3)
    end2 = time.time()
    print(u"Breadth First Travel (from 3):")
    print(basic_graph.breadth_first_traversal(3))
    print(u"Took {} seconds".format(end2-start2))

    crazy_graph = SimpleGraph()
    crazy_dict = {'head': range(100)}
    for num in range(100):
        crazy_dict[num] = ['many']
    crazy_dict[1] = ['single']
    crazy_dict['many'] = []
    crazy_dict['single'] = []
    crazy_graph._graph_content = crazy_dict

    print(u"Made really big graph (100 nodes from head)")
    start3 = time.time()
    crazy_graph.depth_first_traversal('head')
    end3 = time.time()
    print(u"Depth First Travel (from head):")
    print(u"Took {} seconds".format(end3-start3))

    start4 = time.time()
    crazy_graph.breadth_first_traversal('head')
    end4 = time.time()
    print(u"Breadth First Travel (from head):")
    print(u"Took {} seconds".format(end4-start4))
