
.. _API-bitmap-find-next-zero-area-off:

==============================
bitmap_find_next_zero_area_off
==============================

*man bitmap_find_next_zero_area_off(9)*

*4.6.0-rc1*

find a contiguous aligned zero area


Synopsis
========

.. c:function:: unsigned long bitmap_find_next_zero_area_off( unsigned long * map, unsigned long size, unsigned long start, unsigned int nr, unsigned long align_mask, unsigned long align_offset )

Arguments
=========

``map``
    The address to base the search on

``size``
    The bitmap size in bits

``start``
    The bitnumber to start searching at

``nr``
    The number of zeroed bits we're looking for

``align_mask``
    Alignment mask for zero area

``align_offset``
    Alignment offset for zero area.


Description
===========

The ``align_mask`` should be one less than a power of 2; the effect is that the bit offset of all zero areas this function finds plus ``align_offset`` is multiple of that power of
2.
