.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-kmemdup:

============
devm_kmemdup
============

*man devm_kmemdup(9)*

*4.6.0-rc5*

Resource-managed kmemdup


Synopsis
========

.. c:function:: void * devm_kmemdup( struct device * dev, const void * src, size_t len, gfp_t gfp )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
