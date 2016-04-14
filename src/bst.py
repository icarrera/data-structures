from collections import deque


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
        if node:
            node.parent = self


    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node:
            node.parent = self

    @property
    def depth(self):
        try:
            ld = self.left.depth
        except AttributeError:
            ld = 0
        try:
            rd = self.right.depth
        except AttributeError:
            rd = 0
        return max(ld, rd) + 1

    def _disconect(self):
        """Node drops its parent and its parent drops this node."""
        if self._parent:
            if self._parent.left == self:
                self._parent._left = None
            else:
                self._parent._right = None

    def _search(self, val):
        """Check itself and children if it has val return itself if true."""
        if self.val == val:
            return self
        if self.left:
            left_search = self.left._search(val)
            if left_search:
                if left_search.val == val:
                    return left_search
        if self.right:
            right_search = self.right._search(val)
            if right_search:
                if right_search.val == val:
                    return right_search

    def _replace(self):
        """Check each child stack to find the val should be replaced by."""
        if (not self.left and not self.right):
            # if the node is a left end the recursion and return itself.
            rtn_val = self.val
            self._disconect()
            return rtn_val
        left_depth, right_depth = self.left.depth, self.right.depth
        if left_depth > right_depth:
            rtn_val = self.val
            self.val = self.left._replace()
            return rtn_val
        elif right_depth > left_depth:
            rtn_val = self.val
            self.val = self.right._replace()
            return rtn_val
        else:
            if self._parent and self._parent.left == self:
                rtn_val = self.val
                self.val = self.left._replace()
                return rtn_val
            else:
                rtn_val = self.val
                self.val = self.right._replace()
                return rtn_val

    def in_order(self):
        if self._left:
            for val in self._left.in_order():
                yield val
        yield self.val
        if self._right:
            for val in self._right.in_order():
                yield val

    def pre_order(self):
        yield self.val
        if self._left:
            for val in self._left.in_order():
                yield val
        if self._right:
            for val in self._right.in_order():
                yield val

    def post_order(self):
        if self._left:
            for val in self._left.in_order():
                yield val
        if self._right:
            for val in self._right.in_order():
                yield val
        yield self.val

    def rotate_right(self):
        self.parent.left = self.right
        self.right = self.parent

    def rotate_left(self):
        self.parent.right = self.left
        self.left = self.parent


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
                    cursor = parent.left
                    if not side:
                        side = 'left'
                else:
                    cursor = parent.right
                    if not side:
                        side = 'right'
            # create new node object, pass parent to Node constructor
            node = Node(val, parent)
            # If this is the first node connected to a parent increase depth
            if not parent.left and not parent.right:
                depth += 1
            # Connect the new node to the parent based on value.
            if val < parent.val:
                parent.left = node
            else:
                parent.right = node
            # Change the depth if necessary
            if side == 'left' and depth > self.depth_left:
                self.depth_left = depth
            elif side == 'right' and depth > self.depth_right:
                self.depth_right = depth
        # set will add val to node_set if not present already.
        self.node_set.add(val)
        self.balancer()

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
        try:
            return getattr(self._head.left, 'depth', 0) - getattr(self._head.right, 'depth', 0)
        except AttributeError:
            return 0

    def _search(self, val):
        """Return a Node with val if it exists"""
        if self.contains(val):
            return self._head._search(val)

    def in_order(self):
        """Invoke in_order traversal on head node."""
        try:
            return self._head.in_order()
        except AttributeError:
            return []

    def pre_order(self):
        """Invoke pre_order traversal on head node."""
        try:
            return self._head.pre_order()
        except AttributeError:
            return []

    def post_order(self):
        """Invoke post_order traversal on head node."""
        try:
            return self._head.post_order()
        except AttributeError:
            return []

    def breadth_first(self):
        """Perform breadth first traversal of BST."""
        if self._head:
            queue = deque()
            queue.append(self._head)
            while len(queue):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                yield popped.val

    def delete(self, val):
        """Remove Val from the list if present."""
        if self.contains(val):
            deleted = self._search(val)
            if self.depth() == 1:  # One node in tree
                self._head = None
                self.node_set.remove(val)
            # node is a leaf (no children)
            elif (not deleted.left and not deleted.right):
                deleted._disconect()
                self.node_set.remove(val)
            # node has one child
            elif ((deleted.left and not deleted.right) or
                  (deleted.right and not deleted.left)):
                if deleted._parent.left == deleted:
                    try:
                        deleted._parent.left = deleted.left
                        self.node_set.remove(val)
                    except AttributeError:
                        pass
                else:
                    try:
                        deleted._parent.right = deleted.right
                        self.node_set.remove(val)
                    except AttributeError:
                        pass
            # node has two childs
            else:
                deleted._replace()
                self.node_set.remove(val)
        self.balancer()

    def balancer(self):
        """Balancer function to ensure a tree remains balanced."""
        if abs(self.balance()) > 1:
            rotate_node = self._head
            L = 'L'
            R = 'R'
            path = []
            while len(path) + 2 < self.depth():     # Len(path) + 2 arives at the lowest parent node in the tree.
                """If tree is unbalanced, iterate through path to most unbalanced parent."""
                if getattr(rotate_node.left, 'depth', 0) > getattr(rotate_node.right, 'depth', 0):
                    rotate_node = rotate_node.left
                    path.append(L)
                else:
                    rotate_node = rotate_node.right
                    path.append(R)
            if path[-1] == path[-2]:
                """Actions to take if left-Left or right-right path (single rotation)."""
                if path[-1] == L:
                    """Action to take if last step was left (right rotation)"""
                    new_parent = rotate_node.parent.parent
                    rotate_node.rotate_right()
                    new_parent.left = rotate_node
                else:
                    """Action to take if last step was right (left rotation)"""
                    new_parent = rotate_node.parent.parent
                    rotate_node.rotate_left()
                    new_parent.right = rotate_node
            else:
                """Actions to take if left-right or right-left path (double rotation)."""
                if path[-1] == L:
                    """Action to take if last step was left (right rotation followed by left rotation)"""
                    new_parent = rotate_node.parent.parent
                    rotate_node.rotate_right()
                    rotate_node.parent.rotate_left()
                    new_parent.left = rotate_node
                else:
                    """Action to take if last step was right (left rotation followed by right rotation)"""
                    new_parent = rotate_node.parent.parent
                    rotate_node.rotate_left()
                    rotate_node.parent.rotate_right()
                    new_parent.right = rotate_node
