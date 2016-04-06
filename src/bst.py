class Node(object):
    def __init__(self, val=None, parent=None):
        """Init method for Node Class."""
        self.val = val
        self._left = None
        self._right = None
        self._parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        node.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        node.parent = self


class BST(object):

    def __init__(self):
        """Init method for Binary Search Tree."""
        self.node_set = set()
        self._head = None
        self.depth_left = 0
        self.depth_right = 0

    def insert(self, val):
        """Insert node into BST."""
        # check if BST is empty
        if not self._head:
            # if empty, set head to new Node instance
            self._head = Node(val)
        # if not empty BST, check if val is in node_set
        elif val not in self.node_set:
            # set cursor to BST head node
            cursor = self._head
            # set parent node as current cursor (used to set node's parent)
            parent = cursor
            # while cursor is not none...
            while cursor is not None:
                # check if value is less than cursor
                if val < cursor.val:
                    # if val less than cursor val, set cursor to parent._left
                    cursor = parent._left
                # if val was greater than cursor
                else:
                    # if val greater than cursor val, set cursor to parent._right
                    cursor = parent._right
            # create new node object, pass parent to Node constructor
            node = Node(val, parent)
            # if val less than cursor, set parent._left to node
            if val < cursor.val:
                parent._left = node
            # if val greater than cursor, set parent._right to node
            else:
                parent._right = node

        self.node_set.add(val)

    def contains(self, val):
        """Return true if node value present in tree."""
        return val in self.node_set

    def size(self):
        """Return size of BST."""
        return len(self.node_set)
