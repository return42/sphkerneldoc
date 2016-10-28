.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bitmap.h

.. _`bitmap_find_next_zero_area`:

bitmap_find_next_zero_area
==========================

.. c:function:: unsigned long bitmap_find_next_zero_area(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, unsigned long align_mask)

    find a contiguous aligned zero area

    :param unsigned long \*map:
        The address to base the search on

    :param unsigned long size:
        The bitmap size in bits

    :param unsigned long start:
        The bitnumber to start searching at

    :param unsigned int nr:
        The number of zeroed bits we're looking for

    :param unsigned long align_mask:
        Alignment mask for zero area

.. _`bitmap_find_next_zero_area.description`:

Description
-----------

The \ ``align_mask``\  should be one less than a power of 2; the effect is that
the bit offset of all zero areas this function finds is multiples of that
power of 2. A \ ``align_mask``\  of 0 means no alignment is required.

.. This file was automatic generated / don't edit.

