.. -*- coding: utf-8; mode: rst -*-

.. _API-idr-alloc-cyclic:

================
idr_alloc_cyclic
================

*man idr_alloc_cyclic(9)*

*4.6.0-rc5*

allocate new idr entry in a cyclical fashion


Synopsis
========

.. c:function:: int idr_alloc_cyclic( struct idr * idr, void * ptr, int start, int end, gfp_t gfp_mask )

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

Essentially the same as idr_alloc, but prefers to allocate
progressively higher ids if it can. If the “cur” counter wraps, then it
will start again at the “start” end of the range and allocate one that
has already been used.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
