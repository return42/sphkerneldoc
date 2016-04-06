
.. _API-kmem-cache-alloc:

================
kmem_cache_alloc
================

*man kmem_cache_alloc(9)*

*4.6.0-rc1*

Allocate an object


Synopsis
========

.. c:function:: void ⋆ kmem_cache_alloc( struct kmem_cache * cachep, gfp_t flags )

Arguments
=========

``cachep``
    The cache to allocate from.

``flags``
    See ``kmalloc``.


Description
===========

Allocate an object from this cache. The flags are only relevant if the cache has no available objects.
