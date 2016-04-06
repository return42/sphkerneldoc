
.. _API-kmem-cache-free:

===============
kmem_cache_free
===============

*man kmem_cache_free(9)*

*4.6.0-rc1*

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
