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

.. _`bitmap_from_u64`:

BITMAP_FROM_U64
===============

.. c:function::  BITMAP_FROM_U64( n)

    Represent u64 value in the format suitable for bitmap.

    :param  n:
        u64 value

.. _`bitmap_from_u64.description`:

Description
-----------

Linux bitmaps are internally arrays of unsigned longs, i.e. 32-bit
integers in 32-bit environment, and 64-bit integers in 64-bit one.

There are four combinations of endianness and length of the word in linux
ABIs: LE64, BE64, LE32 and BE32.

On 64-bit kernels 64-bit LE and BE numbers are naturally ordered in
bitmaps and therefore don't require any special handling.

On 32-bit kernels 32-bit LE ABI orders lo word of 64-bit number in memory
prior to hi, and 32-bit BE orders hi word prior to lo. The bitmap on the
other hand is represented as an array of 32-bit words and the position of
bit N may therefore be calculated as: word #(N/32) and bit #(N%32) in that
word.  For example, bit #42 is located at 10th position of 2nd word.
It matches 32-bit LE ABI, and we can simply let the compiler store 64-bit
values in memory as it usually does. But for BE we need to swap hi and lo
words manually.

With all that, the macro \ :c:func:`BITMAP_FROM_U64`\  does explicit reordering of hi and
lo parts of u64.  For LE32 it does nothing, and for BE environment it swaps
hi and lo words, as is expected by bitmap.

.. _`bitmap_from_u64`:

bitmap_from_u64
===============

.. c:function:: void bitmap_from_u64(unsigned long *dst, u64 mask)

    Check and swap words within u64.

    :param unsigned long \*dst:
        destination bitmap

    :param u64 mask:
        source bitmap

.. _`bitmap_from_u64.description`:

Description
-----------

In 32-bit Big Endian kernel, when using ``(u32 *)(&val)[*]``
to read u64 mask, we will get the wrong word.
That is ``(u32 *)(&val)[0]`` gets the upper 32 bits,
but we expect the lower 32-bits of u64.

.. This file was automatic generated / don't edit.

