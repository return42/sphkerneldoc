
.. _API-vzalloc-node:

============
vzalloc_node
============

*man vzalloc_node(9)*

*4.6.0-rc1*

allocate memory on a specific node with zero fill


Synopsis
========

.. c:function:: void ⋆ vzalloc_node( unsigned long size, int node )

Arguments
=========

``size``
    allocation size

``node``
    numa node


Description
===========

Allocate enough pages to cover ``size`` from the page level allocator and map them into contiguous kernel virtual space. The memory allocated is set to zero.

For tight control over page level allocator and protection flags use ``__vmalloc_node`` instead.
