.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-alloc:

=========
idr_alloc
=========

*man idr_alloc(9)*

*4.6.0-rc5*

allocate new idr entry


Synopsis
========

.. c:function:: int idr_alloc( struct idr * idr, void * ptr, int start, int end, gfp_t gfp_mask )

Arguments
=========

``idr``
    the (initialized) idr

``ptr``
    pointer to be associated with the new id

``start``
    the minimum id (inclusive)

``end``
    the maximum id (exclusive, <= 0 for max)

``gfp_mask``
    memory allocation flags


Description
===========

Allocate an id in [start, end) and associate it with ``ptr``. If no ID
is available in the specified range, returns -ENOSPC. On memory
allocation failure, returns -ENOMEM.

Note that ``end`` is treated as max when <= 0. This is to always allow
using ``start`` + N as ``end`` as long as N is inside integer range.

The user is responsible for exclusively synchronizing all operations
which may modify ``idr``. However, read-only accesses such as
``idr_find`` or iteration can be performed under RCU read lock provided
the user destroys ``ptr`` in RCU-safe way after removal from idr.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
