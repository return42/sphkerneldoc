.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/bitmap.h

.. _`bitmap-overview`:

bitmap overview
===============

The available bitmap operations and their rough meaning in the
case that the bitmap is a single unsigned long are thus:

Note that nbits should be always a compile time evaluable constant.
Otherwise many inlines will generate horrible code.

::

 bitmap_zero(dst, nbits)                     *dst = 0UL
 bitmap_fill(dst, nbits)                     *dst = ~0UL
 bitmap_copy(dst, src, nbits)                *dst = *src
 bitmap_and(dst, src1, src2, nbits)          *dst = *src1 & *src2
 bitmap_or(dst, src1, src2, nbits)           *dst = *src1 | *src2
 bitmap_xor(dst, src1, src2, nbits)          *dst = *src1 ^ *src2
 bitmap_andnot(dst, src1, src2, nbits)       *dst = *src1 & ~(*src2)
 bitmap_complement(dst, src, nbits)          *dst = ~(*src)
 bitmap_equal(src1, src2, nbits)             Are *src1 and *src2 equal?
 bitmap_intersects(src1, src2, nbits)        Do *src1 and *src2 overlap?
 bitmap_subset(src1, src2, nbits)            Is *src1 a subset of *src2?
 bitmap_empty(src, nbits)                    Are all bits zero in *src?
 bitmap_full(src, nbits)                     Are all bits set in *src?
 bitmap_weight(src, nbits)                   Hamming Weight: number set bits
 bitmap_set(dst, pos, nbits)                 Set specified bit area
 bitmap_clear(dst, pos, nbits)               Clear specified bit area
 bitmap_find_next_zero_area(buf, len, pos, n, mask)  Find bit free area
 bitmap_find_next_zero_area_off(buf, len, pos, n, mask)  as above
 bitmap_shift_right(dst, src, n, nbits)      *dst = *src >> n
 bitmap_shift_left(dst, src, n, nbits)       *dst = *src << n
 bitmap_remap(dst, src, old, new, nbits)     *dst = map(old, new)(src)
 bitmap_bitremap(oldbit, old, new, nbits)    newbit = map(old, new)(oldbit)
 bitmap_onto(dst, orig, relmap, nbits)       *dst = orig relative to relmap
 bitmap_fold(dst, orig, sz, nbits)           dst bits = orig bits mod sz
 bitmap_parse(buf, buflen, dst, nbits)       Parse bitmap dst from kernel buf
 bitmap_parse_user(ubuf, ulen, dst, nbits)   Parse bitmap dst from user buf
 bitmap_parselist(buf, dst, nbits)           Parse bitmap dst from kernel buf
 bitmap_parselist_user(buf, dst, nbits)      Parse bitmap dst from user buf
 bitmap_find_free_region(bitmap, bits, order)  Find and allocate bit region
 bitmap_release_region(bitmap, pos, order)   Free specified bit region
 bitmap_allocate_region(bitmap, pos, order)  Allocate specified bit region
 bitmap_from_u32array(dst, nbits, buf, nwords)  *dst = *buf (nwords 32b words)
 bitmap_to_u32array(buf, nwords, src, nbits) *buf = *dst (nwords 32b words)

.. _`bitmap-bitops`:

bitmap bitops
=============

Also the following operations in asm/bitops.h apply to bitmaps.::

 set_bit(bit, addr)                  *addr |= bit
 clear_bit(bit, addr)                *addr &= ~bit
 change_bit(bit, addr)               *addr ^= bit
 test_bit(bit, addr)                 Is bit set in *addr?
 test_and_set_bit(bit, addr)         Set bit and return old value
 test_and_clear_bit(bit, addr)       Clear bit and return old value
 test_and_change_bit(bit, addr)      Change bit and return old value
 find_first_zero_bit(addr, nbits)    Position first zero bit in *addr
 find_first_bit(addr, nbits)         Position first set bit in *addr
 find_next_zero_bit(addr, nbits, bit)  Position next zero bit in *addr >= bit
 find_next_bit(addr, nbits, bit)     Position next set bit in *addr >= bit

.. _`declare-bitmap`:

declare bitmap
==============

The DECLARE_BITMAP(name,bits) macro, in linux/types.h, can be used
to declare an array named 'name' of just enough unsigned longs to
contain all bit positions from 0 to 'bits' - 1.

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

