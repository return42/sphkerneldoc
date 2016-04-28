.. -*- coding: utf-8; mode: rst -*-

.. _API-kmem-cache-alloc:

================
kmem_cache_alloc
================

*man kmem_cache_alloc(9)*

*4.6.0-rc5*

Allocate an object


Synopsis
========

.. c:function:: void * kmem_cache_alloc( struct kmem_cache * cachep, gfp_t flags )

Arguments
=========

``cachep``
    The cache to allocate from.

``flags``
    See ``kmalloc``.


Description
===========

Allocate an object from this cache. The flags are only relevant if the
cache has no available objects.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
