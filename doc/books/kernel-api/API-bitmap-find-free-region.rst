
.. _API-bitmap-find-free-region:

=======================
bitmap_find_free_region
=======================

*man bitmap_find_free_region(9)*

*4.6.0-rc1*

find a contiguous aligned mem region


Synopsis
========

.. c:function:: int bitmap_find_free_region( unsigned long * bitmap, unsigned int bits, int order )

Arguments
=========

``bitmap``
    array of unsigned longs corresponding to the bitmap

``bits``
    number of bits in the bitmap

``order``
    region size (log base 2 of number of bits) to find


Description
===========

Find a region of free (zero) bits in a ``bitmap`` of ``bits`` bits and allocate them (set them to one). Only consider regions of length a power (``order``) of two, aligned to that
power of two, which makes the search algorithm much faster.

Return the bit offset in bitmap of the allocated region, or -errno on failure.
