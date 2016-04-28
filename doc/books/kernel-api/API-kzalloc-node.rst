.. -*- coding: utf-8; mode: rst -*-

.. _API-kzalloc-node:

============
kzalloc_node
============

*man kzalloc_node(9)*

*4.6.0-rc5*

allocate zeroed memory from a particular memory node.


Synopsis
========

.. c:function:: void * kzalloc_node( size_t size, gfp_t flags, int node )

Arguments
=========

``size``
    how many bytes of memory are required.

``flags``
    the type of memory to allocate (see kmalloc).

``node``
    memory node from which to allocate


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
