
.. _API-bitmap-allocate-region:

======================
bitmap_allocate_region
======================

*man bitmap_allocate_region(9)*

*4.6.0-rc1*

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

Return 0 on success, or ``-EBUSY`` if specified region wasn't free (not all bits were zero).
