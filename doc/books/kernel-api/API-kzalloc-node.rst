
.. _API-kzalloc-node:

============
kzalloc_node
============

*man kzalloc_node(9)*

*4.6.0-rc1*

allocate zeroed memory from a particular memory node.


Synopsis
========

.. c:function:: void ⋆ kzalloc_node( size_t size, gfp_t flags, int node )

Arguments
=========

``size``
    how many bytes of memory are required.

``flags``
    the type of memory to allocate (see kmalloc).

``node``
    memory node from which to allocate
