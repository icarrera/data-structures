# data-structures
Code Fellows Python 401 Data Structures assignment
Created by Kyle Richardson and Iris Carrera
This repo will hold sample code for a number of classic data structures implemented in Python.

## linked_list.py
The linked list data structure. Our design uses Node objects where each node containing a value and a pointer to some other node, or a None value if it's the last in the list. This None value pointer makes reading through the list for various functions very easy as we can just do while head_step: and have the head_step assigned to the current node's point_to. That will go through each item until head_step will be assigned to None value stopping the loop. In general our outside resources included Python documentation and assistance from our instructors.

## stack.py
The Stack data structure. We realized that a stack is essentially just a linked_list. Since the linked_list we made has all the qualities of a Stack data structure including the LIFO access. We decided to inherit the LinkedList class for the Stack class and override the pop() method from LinkedList. And add a method push(val). In both cases we just used methods from the LinkedList class to create these methods as the LinkedList methods did everything we already needed to do.

## dll.py
The doubly linked list data structure. To implement the DLL we modified our Node objects to contain two pointers, one to to the next_node and one to the prev_node. The prev_node has a None value if it's the head and the next_node has a None value if it's the tail. In all cases we had to overwrite functions since we needed to handle both links, which was not provided in our linked list.

## queue.py
The queue data structure. We decided to use a composition of a Doubly linked list as a container for the queue. Since a queue primarily cares about adding stuff at the end and grabbing stuff from the front all of which our DLL already supports. So each method in queue is just calling an already existing method or property the container has. Makes life a lot easier.

## parenthetic.py
A simple single function script which has a function that takes a unicode string and deterimes if all parenthetics in it are properly ordered and closed. At first it seemed like the best option was to add everything to a queue to check out but I found it was a little easier just to do all the checking while going through the characters of the string.
