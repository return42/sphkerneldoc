.. -*- coding: utf-8; mode: rst -*-

.. _API-vmalloc-node:

============
vmalloc_node
============

*man vmalloc_node(9)*

*4.6.0-rc5*

allocate memory on a specific node


Synopsis
========

.. c:function:: void * vmalloc_node( unsigned long size, int node )

Arguments
=========

``size``
    allocation size

``node``
    numa node


Description
===========

Allocate enough pages to cover ``size`` from the page level allocator
and map them into contiguous kernel virtual space.

For tight control over page level allocator and protection flags use
``__vmalloc`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
