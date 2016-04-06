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
            self._head = Node(val)
            # set depth_L/R to 1 (one level present)
            self.depth_left = 1
            self.depth_right = 1
        # if not empty BST, check if val is in node_set
        elif val not in self.node_set:
            cursor = self._head
            parent = cursor
            side = None
            depth = 0
            while cursor:
                parent = cursor
                depth += 1
                if val < cursor.val:
                    cursor = parent._left
                    if side is None:
                        side = 'left'
                else:
                    cursor = parent._right
                    if side is None:
                        side = 'right'
            # create new node object, pass parent to Node constructor
            node = Node(val, parent)
            # If this is the first node connected to a parent increase depth
            if not parent._left and not parent._right:
                depth += 1
            # Connect the new node to the parent based on value.
            if val < parent.val:
                parent._left = node
            else:
                parent._right = node
            # Change the depth if necessary
            if side == 'left' and depth > self.depth_left:
                self.depth_left = depth
            elif side == 'right' and depth > self.depth_right:
                self.depth_right = depth
        # set will add val to node_set if not present already.
        self.node_set.add(val)

    def contains(self, val):
        """Return true if node value present in tree."""
        return val in self.node_set

    def size(self):
        """Return size of BST."""
        return len(self.node_set)

    def depth(self):
        """Return depth of BST."""
        return max(self.depth_left, self.depth_right)

    def balance(self):
        """Return diffence of depth_left and depth_right."""
        return self.depth_left - self.depth_right
