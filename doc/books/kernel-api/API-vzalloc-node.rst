.. -*- coding: utf-8; mode: rst -*-

.. _API-vzalloc-node:

============
vzalloc_node
============

*man vzalloc_node(9)*

*4.6.0-rc5*

allocate memory on a specific node with zero fill


Synopsis
========

.. c:function:: void * vzalloc_node( unsigned long size, int node )

Arguments
=========

``size``
    allocation size

``node``
    numa node


Description
===========

Allocate enough pages to cover ``size`` from the page level allocator
and map them into contiguous kernel virtual space. The memory allocated
is set to zero.

For tight control over page level allocator and protection flags use
``__vmalloc_node`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
