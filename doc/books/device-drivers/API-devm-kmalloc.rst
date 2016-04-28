.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-kmalloc:

============
devm_kmalloc
============

*man devm_kmalloc(9)*

*4.6.0-rc5*

Resource-managed kmalloc


Synopsis
========

.. c:function:: void * devm_kmalloc( struct device * dev, size_t size, gfp_t gfp )

Arguments
=========

``dev``
    Device to allocate memory for

``size``
    Allocation size

``gfp``
    Allocation gfp flags


Description
===========

Managed kmalloc. Memory allocated with this function is automatically
freed on driver detach. Like all other devres resources, guaranteed
alignment is unsigned long long.


RETURNS
=======

Pointer to allocated memory on success, NULL on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
