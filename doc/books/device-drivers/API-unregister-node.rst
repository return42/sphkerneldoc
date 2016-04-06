
.. _API-unregister-node:

===============
unregister_node
===============

*man unregister_node(9)*

*4.6.0-rc1*

unregister a node device


Synopsis
========

.. c:function:: void unregister_node( struct node * node )

Arguments
=========

``node``
    node going away


Description
===========

Unregisters a node device ``node``. All the devices on the node must be unregistered before calling this function.
