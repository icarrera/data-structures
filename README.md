[![Build Status](https://travis-ci.org/KyleRichVA/data-structures.svg?branch=master)](https://travis-ci.org/KyleRichVA/data-structures)
# data-structures
Code Fellows Python 401 Data Structures assignment
Created by Kyle Richardson and Iris Carrera
This repo will hold sample code for a number of classic data structures implemented in Python.

## linked_list.py
The linked list data structure. Our design uses Node objects where each node containing a value and a pointer to some other node, or a None value if it's the last in the list. This None value pointer makes reading through the list for various functions very easy as we can just do while head_step: and have the head_step assigned to the current node's point_to. That will go through each item until head_step will be assigned to None value stopping the loop. In general our outside resources included Python documentation and assistance from our instructors.

## stack.py
The Stack data structure. We realized that a stack is essentially just a linked_list. Since the linked_list we made has all the qualities of a Stack data structure including the LIFO access. We decided to inherit the LinkedList class for the Stack class and override the pop() method from LinkedList. And add a method push(val). In both cases we just used methods from the LinkedList class to create these methods as the LinkedList methods did everything we already needed to do.

## dll.py
The doubly linked list data structure. To implement the DLL we created a new Node object to contain two pointers, one to to the next_node and one to the prev_node. The prev_node has a None value if it's the head and the next_node has a None value if it's the tail. In all cases we had to overwrite functions since we needed to handle both links, which was not provided in our linked list.

## queue.py
The queue data structure. We decided to use a composition of a Doubly Linked List as a container for the queue. Since a queue primarily cares about adding stuff at the end and grabbing stuff from the front all of which our DLL already supports. So each method in queue is just calling an already existing method or property the container has. Makes life a lot easier.

## deque.py
The deque data structure. We use a composotion of a Doubly Linked List as a container for the deque because we add and remove values from both the front and back of our deque. It was not ideal to inherit from queue because we would have to overwrite most of queue's functions.

## binheap.py
The binary heap data structure. We created a max heap data structure wherein the parent value must be greater than that of its children. We created a push() method that adds a new value to our heap, maintaining the heap property. Our push method then checks if value of child is greater or less than parent. If true, we switch the values then run the same check on the new parent and its parent. We also created a .pop() method, which removes the "top" value in the heap, maintaining the heap property. Our pop method then checks if the value of a child is greater or less than parent. Does a switch if this is true then runs the check on the new parent and its parent.

## pqueue.py
The Priority Queue data structure. This contains a Binary Heap object as that allows us an easy way to make sure that the items in the queue are in order based off priority and the order of when it placed in. We decided to make a new Class called PriorityQueueItem that contains some value and a priority number. We then set the less than and greater than properties of this class to do this greater than/less than checking on the priority value of the items. Allowing us to use everything in the Binary Heap class without any major changes to correctly sort the queue when adding and removing items.

## simple_graph.py
The Simple Graph data structure. In this case we started from scratch and contained everything inside a dictonary. Each key refers to a node and the node's value is a list of nodes it has edges going to. Since we used a dictonary many of the methods created utilize built-in features of the dictonary and list to accomplish our tasks.

## traversal
Continuation of the Graph data structure. We added Breadth-first Search and Depth-first Search methods to our our SimpleGraph class. Breadth-first search starts at a given node and explores the neighbor nodes first, before moving to the next level neighbors. Depth-first search starts at a given node and explores as far as possible along each branch before backtracking. Both return the full visited path when their traversal is complete.

## weighted edges
Continuation of the Graph data structure. We added weighted edges to our Graph data structure and adjusted our methods to work with weighted edges. Our graph contents are still in a dictionary, with some modifications. Each key still refers to a node but now that node's value is a list of dictionaries. Each inner-dictionary has the pointed-to node as a key. The pointed-to node's value is the weighted-edge. 

## bst.py
The Binary Search Tree. Currently can append nodes and traverse the tree through a variaty of ways. The tree is a combination of many nodes each with a left and right property. Adding to the node is dependent of the values of the node and which is greater than the other. Traversal is done through recursive generators mostly except for breadth first which uses a generator with a deque counter keeping track of the proper order to return node values.
