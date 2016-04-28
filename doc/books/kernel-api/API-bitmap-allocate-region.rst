.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-allocate-region:

======================
bitmap_allocate_region
======================

*man bitmap_allocate_region(9)*

*4.6.0-rc5*

allocate bitmap region


Synopsis
========

.. c:function:: int bitmap_allocate_region( unsigned long * bitmap, unsigned int pos, int order )

Arguments
=========

``bitmap``
    array of unsigned longs corresponding to the bitmap

``pos``
    beginning of bit region to allocate

``order``
    region size (log base 2 of number of bits) to allocate


Description
===========

Allocate (set bits in) a specified region of a bitmap.

Return 0 on success, or ``-EBUSY`` if specified region wasn't free (not
all bits were zero).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
