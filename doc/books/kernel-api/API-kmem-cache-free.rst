.. -*- coding: utf-8; mode: rst -*-

.. _API-kmem-cache-free:

===============
kmem_cache_free
===============

*man kmem_cache_free(9)*

*4.6.0-rc5*

Deallocate an object


Synopsis
========

.. c:function:: void kmem_cache_free( struct kmem_cache * cachep, void * objp )

Arguments
=========

``cachep``
    The cache the allocation was from.

``objp``
    The previously allocated object.


Description
===========

Free an object which was previously allocated from this cache.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
