
.. _API-find-next-best-node:

===================
find_next_best_node
===================

*man find_next_best_node(9)*

*4.6.0-rc1*

find the next node that should appear in a given node's fallback list


Synopsis
========

.. c:function:: int find_next_best_node( int node, nodemask_t * used_node_mask )

Arguments
=========

``node``
    node whose fallback list we're appending

``used_node_mask``
    nodemask_t of already used nodes


Description
===========

We use a number of factors to determine which is the next node that should appear on a given node's fallback list. The node should not have appeared already in ``node``'s fallback
list, and it should be the next closest node according to the distance array (which contains arbitrary distance values from each node to each node in the system), and should also
prefer nodes with no CPUs, since presumably they'll have very little allocation pressure on them otherwise. It returns -1 if no node is found.
