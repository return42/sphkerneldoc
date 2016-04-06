
.. _API-vmalloc-node:

============
vmalloc_node
============

*man vmalloc_node(9)*

*4.6.0-rc1*

allocate memory on a specific node


Synopsis
========

.. c:function:: void ⋆ vmalloc_node( unsigned long size, int node )

Arguments
=========

``size``
    allocation size

``node``
    numa node


Description
===========

Allocate enough pages to cover ``size`` from the page level allocator and map them into contiguous kernel virtual space.

For tight control over page level allocator and protection flags use ``__vmalloc`` instead.
