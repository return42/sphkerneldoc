
.. _API-devm-kmemdup:

============
devm_kmemdup
============

*man devm_kmemdup(9)*

*4.6.0-rc1*

Resource-managed kmemdup


Synopsis
========

.. c:function:: void ⋆ devm_kmemdup( struct device * dev, const void * src, size_t len, gfp_t gfp )

Arguments
=========

``dev``
    Device this memory belongs to

``src``
    Memory region to duplicate

``len``
    Memory region length

``gfp``
    GFP mask to use


Description
===========

Duplicate region of a memory using resource managed kmalloc
