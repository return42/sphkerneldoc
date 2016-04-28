.. -*- coding: utf-8; mode: rst -*-

.. _API-kmem-cache-alloc-node:

=====================
kmem_cache_alloc_node
=====================

*man kmem_cache_alloc_node(9)*

*4.6.0-rc5*

Allocate an object on the specified node


Synopsis
========

.. c:function:: void * kmem_cache_alloc_node( struct kmem_cache * cachep, gfp_t flags, int nodeid )

Arguments
=========

``cachep``
    The cache to allocate from.

``flags``
    See ``kmalloc``.

``nodeid``
    node number of the target node.


Description
===========

Identical to kmem_cache_alloc but it will allocate memory on the given
node, which can improve the performance for cpu bound structures.

Fallback to other node is possible if __GFP_THISNODE is not set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
