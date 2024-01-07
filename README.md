# Wireless_is_the_New_Fiber
## This code is an implementation of ICPC 2018 Problem K that states : 

A new type of unbounded-bandwidth wireless communication has just been tested and proved to be a
suitable replacement for the existing, fiber-based communications network, which is struggling to keep
up with traffic growth.The new communications network will not have any fiber. Instead, it will have wireless links, each
connecting two nodes. These links have unbounded bandwidth but are expensive, so it has been decided
that as few of these links will be built as possible to provide connectivity; for each pair of nodes there
should be exactly one way to travel between them along the wireless links.Your task is to design the new network so that it has precisely one path between each pair of nodes while
minimizing the number of nodes that do not have the same number of connections as in the original
network.

## The code implemented focusses on 
focuses on removing redundant links found between fiber-based communications network, given as a graph, and convert it into an optimal tree data structure thereby making the connections ‘Wireless’ using the greedy algorithm and python as the programming language.
We calculate the inorder degree of the nodes, take the node with the highest degree and connect it with the remaining nodes
