class Node(object):
    def __init__(self, val):
        """Init method for Node Class."""
        self.val = val
        self._left = None
        self._right = None
        self.has_parent = False

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        node.has_parent = True

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        node.has_parent = True


class BST(object):

    def __init__(self):
        """Init method for Binary Search Tree."""
        self.node_set = set()
        self._head = None


