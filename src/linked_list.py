# -*- coding: utf-8-*-
import string

class LinkedList(object):
    def __init__(self, iter=None):
        self.head = None
        if iter:
            for val in iter:
                self.insert(val)

    def insert(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        try:
            rtn_value = self.head.val
            new_head = self.head.next_node
            self.head = new_head
            return rtn_value
        except AttributeError:
            return None

    def size(self):
        count = 0
        step_head = self.head
        while step_head:
            count += 1
            step_head = step_head.next_node
        return count
    def search(self, val):

        step_head = self.head
        while step_head:
            if step_head.val == val:
                return step_head
            step_head = step_head.next_node
        else:
            return None
            
    def remove(self, node):
        step_head = self.head
        prev_node = None
        if self.search(node.val) is None:
            raise ValueError('Node is not in list.')
        while step_head:
            if step_head.val == node.val:
                if prev_node is None:
                    self.head = step_head.next_node
                    step_head = self.head
                else:
                    prev_node.next_node = step_head.next_node
                    step_head = prev_node
            prev_node = step_head
            step_head = step_head.next_node

    def to_string(self):
        rtn_string = u"("
        step_head = self.head
        while step_head:
            if step_head.next_node is None:
                rtn_string = rtn_string + str(step_head.val)
                break
            rtn_string = rtn_string + str(step_head.val) + u", "
            step_head = step_head.next_node
        rtn_string = rtn_string + u")"
        return rtn_string

    def display(self):
        print(self.to_string())


class Node(object):
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
