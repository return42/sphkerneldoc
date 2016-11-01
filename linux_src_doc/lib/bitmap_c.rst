.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/bitmap.c

.. _`__bitmap_shift_right`:

__bitmap_shift_right
====================

.. c:function:: void __bitmap_shift_right(unsigned long *dst, const unsigned long *src, unsigned shift, unsigned nbits)

    logical right shift of the bits in a bitmap

    :param unsigned long \*dst:
        destination bitmap

    :param const unsigned long \*src:
        source bitmap

    :param unsigned shift:
        shift by this many bits

    :param unsigned nbits:
        bitmap size, in bits

.. _`__bitmap_shift_right.description`:

Description
-----------

Shifting right (dividing) means moving bits in the MS -> LS bit
direction.  Zeros are fed into the vacated MS positions and the
LS bits shifted off the bottom are lost.

.. _`__bitmap_shift_left`:

__bitmap_shift_left
===================

.. c:function:: void __bitmap_shift_left(unsigned long *dst, const unsigned long *src, unsigned int shift, unsigned int nbits)

    logical left shift of the bits in a bitmap

    :param unsigned long \*dst:
        destination bitmap

    :param const unsigned long \*src:
        source bitmap

    :param unsigned int shift:
        shift by this many bits

    :param unsigned int nbits:
        bitmap size, in bits

.. _`__bitmap_shift_left.description`:

Description
-----------

Shifting left (multiplying) means moving bits in the LS -> MS
direction.  Zeros are fed into the vacated LS bit positions
and those MS bits shifted off the top are lost.

.. _`bitmap_find_next_zero_area_off`:

bitmap_find_next_zero_area_off
==============================

.. c:function:: unsigned long bitmap_find_next_zero_area_off(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, unsigned long align_mask, unsigned long align_offset)

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

    :param unsigned long align_offset:
        Alignment offset for zero area.

.. _`bitmap_find_next_zero_area_off.description`:

Description
-----------

The \ ``align_mask``\  should be one less than a power of 2; the effect is that
the bit offset of all zero areas this function finds plus \ ``align_offset``\ 
is multiple of that power of 2.

.. _`__bitmap_parse`:

__bitmap_parse
==============

.. c:function:: int __bitmap_parse(const char *buf, unsigned int buflen, int is_user, unsigned long *maskp, int nmaskbits)

    convert an ASCII hex string into a bitmap.

    :param const char \*buf:
        pointer to buffer containing string.

    :param unsigned int buflen:
        buffer size in bytes.  If string is smaller than this
        then it must be terminated with a \0.

    :param int is_user:
        location of buffer, 0 indicates kernel space

    :param unsigned long \*maskp:
        pointer to bitmap array that will contain result.

    :param int nmaskbits:
        size of bitmap, in bits.

.. _`__bitmap_parse.description`:

Description
-----------

Commas group hex digits into chunks.  Each chunk defines exactly 32
bits of the resultant bitmask.  No chunk may specify a value larger
than 32 bits (%-EOVERFLOW), and if a chunk specifies a smaller value
then leading 0-bits are prepended.  \ ``-EINVAL``\  is returned for illegal
characters and for grouping errors such as "1,,5", ",44", "," and "".
Leading and trailing whitespace accepted, but not embedded whitespace.

.. _`bitmap_parse_user`:

bitmap_parse_user
=================

.. c:function:: int bitmap_parse_user(const char __user *ubuf, unsigned int ulen, unsigned long *maskp, int nmaskbits)

    convert an ASCII hex string in a user buffer into a bitmap

    :param const char __user \*ubuf:
        pointer to user buffer containing string.

    :param unsigned int ulen:
        buffer size in bytes.  If string is smaller than this
        then it must be terminated with a \0.

    :param unsigned long \*maskp:
        pointer to bitmap array that will contain result.

    :param int nmaskbits:
        size of bitmap, in bits.

.. _`bitmap_parse_user.description`:

Description
-----------

Wrapper for \__bitmap_parse(), providing it with user buffer.

We cannot have this as an inline function in bitmap.h because it needs
linux/uaccess.h to get the \ :c:func:`access_ok`\  declaration and this causes
cyclic dependencies.

.. _`bitmap_print_to_pagebuf`:

bitmap_print_to_pagebuf
=======================

.. c:function:: int bitmap_print_to_pagebuf(bool list, char *buf, const unsigned long *maskp, int nmaskbits)

    convert bitmap to list or hex format ASCII string

    :param bool list:
        indicates whether the bitmap must be list

    :param char \*buf:
        page aligned buffer into which string is placed

    :param const unsigned long \*maskp:
        pointer to bitmap to convert

    :param int nmaskbits:
        size of bitmap, in bits

.. _`bitmap_print_to_pagebuf.description`:

Description
-----------

Output format is a comma-separated list of decimal numbers and
ranges if list is specified or hex digits grouped into comma-separated
sets of 8 digits/set. Returns the number of characters written to buf.

It is assumed that \ ``buf``\  is a pointer into a PAGE_SIZE area and that
sufficient storage remains at \ ``buf``\  to accommodate the
\ :c:func:`bitmap_print_to_pagebuf`\  output.

.. _`__bitmap_parselist`:

__bitmap_parselist
==================

.. c:function:: int __bitmap_parselist(const char *buf, unsigned int buflen, int is_user, unsigned long *maskp, int nmaskbits)

    convert list format ASCII string to bitmap

    :param const char \*buf:
        read nul-terminated user string from this buffer

    :param unsigned int buflen:
        buffer size in bytes.  If string is smaller than this
        then it must be terminated with a \0.

    :param int is_user:
        location of buffer, 0 indicates kernel space

    :param unsigned long \*maskp:
        write resulting mask here

    :param int nmaskbits:
        number of bits in mask to be written

.. _`__bitmap_parselist.description`:

Description
-----------

Input format is a comma-separated list of decimal numbers and
ranges.  Consecutively set bits are shown as two hyphen-separated
decimal numbers, the smallest and largest bit numbers set in
the range.
Optionally each range can be postfixed to denote that only parts of it
should be set. The range will divided to groups of specific size.
From each group will be used only defined amount of bits.
Syntax: range:used_size/group_size
Example: 0-1023:2/256 ==> 0,1,256,257,512,513,768,769

Returns 0 on success, -errno on invalid input strings.

.. _`__bitmap_parselist.error-values`:

Error values
------------

%-EINVAL: second number in range smaller than first
\ ``-EINVAL``\ : invalid character in string
\ ``-ERANGE``\ : bit number specified too large for mask

.. _`bitmap_parselist_user`:

bitmap_parselist_user
=====================

.. c:function:: int bitmap_parselist_user(const char __user *ubuf, unsigned int ulen, unsigned long *maskp, int nmaskbits)

    :param const char __user \*ubuf:
        pointer to user buffer containing string.

    :param unsigned int ulen:
        buffer size in bytes.  If string is smaller than this
        then it must be terminated with a \0.

    :param unsigned long \*maskp:
        pointer to bitmap array that will contain result.

    :param int nmaskbits:
        size of bitmap, in bits.

.. _`bitmap_parselist_user.description`:

Description
-----------

Wrapper for \ :c:func:`bitmap_parselist`\ , providing it with user buffer.

We cannot have this as an inline function in bitmap.h because it needs
linux/uaccess.h to get the \ :c:func:`access_ok`\  declaration and this causes
cyclic dependencies.

.. _`bitmap_pos_to_ord`:

bitmap_pos_to_ord
=================

.. c:function:: int bitmap_pos_to_ord(const unsigned long *buf, unsigned int pos, unsigned int nbits)

    find ordinal of set bit at given position in bitmap

    :param const unsigned long \*buf:
        pointer to a bitmap

    :param unsigned int pos:
        a bit position in \ ``buf``\  (0 <= \ ``pos``\  < \ ``nbits``\ )

    :param unsigned int nbits:
        number of valid bit positions in \ ``buf``\ 

.. _`bitmap_pos_to_ord.description`:

Description
-----------

Map the bit at position \ ``pos``\  in \ ``buf``\  (of length \ ``nbits``\ ) to the
ordinal of which set bit it is.  If it is not set or if \ ``pos``\ 
is not a valid bit position, map to -1.

If for example, just bits 4 through 7 are set in \ ``buf``\ , then \ ``pos``\ 
values 4 through 7 will get mapped to 0 through 3, respectively,
and other \ ``pos``\  values will get mapped to -1.  When \ ``pos``\  value 7
gets mapped to (returns) \ ``ord``\  value 3 in this example, that means
that bit 7 is the 3rd (starting with 0th) set bit in \ ``buf``\ .

The bit positions 0 through \ ``bits``\  are valid positions in \ ``buf``\ .

.. _`bitmap_ord_to_pos`:

bitmap_ord_to_pos
=================

.. c:function:: unsigned int bitmap_ord_to_pos(const unsigned long *buf, unsigned int ord, unsigned int nbits)

    find position of n-th set bit in bitmap

    :param const unsigned long \*buf:
        pointer to bitmap

    :param unsigned int ord:
        ordinal bit position (n-th set bit, n >= 0)

    :param unsigned int nbits:
        number of valid bit positions in \ ``buf``\ 

.. _`bitmap_ord_to_pos.description`:

Description
-----------

Map the ordinal offset of bit \ ``ord``\  in \ ``buf``\  to its position in \ ``buf``\ .
Value of \ ``ord``\  should be in range 0 <= \ ``ord``\  < weight(buf). If \ ``ord``\ 
>= weight(buf), returns \ ``nbits``\ .

If for example, just bits 4 through 7 are set in \ ``buf``\ , then \ ``ord``\ 
values 0 through 3 will get mapped to 4 through 7, respectively,
and all other \ ``ord``\  values returns \ ``nbits``\ .  When \ ``ord``\  value 3
gets mapped to (returns) \ ``pos``\  value 7 in this example, that means
that the 3rd set bit (starting with 0th) is at position 7 in \ ``buf``\ .

The bit positions 0 through \ ``nbits``\ -1 are valid positions in \ ``buf``\ .

.. _`bitmap_remap`:

bitmap_remap
============

.. c:function:: void bitmap_remap(unsigned long *dst, const unsigned long *src, const unsigned long *old, const unsigned long *new, unsigned int nbits)

    Apply map defined by a pair of bitmaps to another bitmap

    :param unsigned long \*dst:
        remapped result

    :param const unsigned long \*src:
        subset to be remapped

    :param const unsigned long \*old:
        defines domain of map

    :param const unsigned long \*new:
        defines range of map

    :param unsigned int nbits:
        number of bits in each of these bitmaps

.. _`bitmap_remap.description`:

Description
-----------

Let \ ``old``\  and \ ``new``\  define a mapping of bit positions, such that
whatever position is held by the n-th set bit in \ ``old``\  is mapped
to the n-th set bit in \ ``new``\ .  In the more general case, allowing
for the possibility that the weight 'w' of \ ``new``\  is less than the
weight of \ ``old``\ , map the position of the n-th set bit in \ ``old``\  to
the position of the m-th set bit in \ ``new``\ , where m == n % w.

If either of the \ ``old``\  and \ ``new``\  bitmaps are empty, or if \ ``src``\  and
\ ``dst``\  point to the same location, then this routine copies \ ``src``\ 
to \ ``dst``\ .

The positions of unset bits in \ ``old``\  are mapped to themselves
(the identify map).

Apply the above specified mapping to \ ``src``\ , placing the result in
\ ``dst``\ , clearing any bits previously set in \ ``dst``\ .

For example, lets say that \ ``old``\  has bits 4 through 7 set, and
\ ``new``\  has bits 12 through 15 set.  This defines the mapping of bit
position 4 to 12, 5 to 13, 6 to 14 and 7 to 15, and of all other
bit positions unchanged.  So if say \ ``src``\  comes into this routine
with bits 1, 5 and 7 set, then \ ``dst``\  should leave with bits 1,
13 and 15 set.

.. _`bitmap_bitremap`:

bitmap_bitremap
===============

.. c:function:: int bitmap_bitremap(int oldbit, const unsigned long *old, const unsigned long *new, int bits)

    Apply map defined by a pair of bitmaps to a single bit

    :param int oldbit:
        bit position to be mapped

    :param const unsigned long \*old:
        defines domain of map

    :param const unsigned long \*new:
        defines range of map

    :param int bits:
        number of bits in each of these bitmaps

.. _`bitmap_bitremap.description`:

Description
-----------

Let \ ``old``\  and \ ``new``\  define a mapping of bit positions, such that
whatever position is held by the n-th set bit in \ ``old``\  is mapped
to the n-th set bit in \ ``new``\ .  In the more general case, allowing
for the possibility that the weight 'w' of \ ``new``\  is less than the
weight of \ ``old``\ , map the position of the n-th set bit in \ ``old``\  to
the position of the m-th set bit in \ ``new``\ , where m == n % w.

The positions of unset bits in \ ``old``\  are mapped to themselves
(the identify map).

Apply the above specified mapping to bit position \ ``oldbit``\ , returning
the new bit position.

For example, lets say that \ ``old``\  has bits 4 through 7 set, and
\ ``new``\  has bits 12 through 15 set.  This defines the mapping of bit
position 4 to 12, 5 to 13, 6 to 14 and 7 to 15, and of all other
bit positions unchanged.  So if say \ ``oldbit``\  is 5, then this routine
returns 13.

.. _`bitmap_onto`:

bitmap_onto
===========

.. c:function:: void bitmap_onto(unsigned long *dst, const unsigned long *orig, const unsigned long *relmap, unsigned int bits)

    translate one bitmap relative to another

    :param unsigned long \*dst:
        resulting translated bitmap

    :param const unsigned long \*orig:
        original untranslated bitmap

    :param const unsigned long \*relmap:
        bitmap relative to which translated

    :param unsigned int bits:
        number of bits in each of these bitmaps

.. _`bitmap_onto.description`:

Description
-----------

Set the n-th bit of \ ``dst``\  iff there exists some m such that the
n-th bit of \ ``relmap``\  is set, the m-th bit of \ ``orig``\  is set, and
the n-th bit of \ ``relmap``\  is also the m-th \_set\_ bit of \ ``relmap``\ .
(If you understood the previous sentence the first time your
read it, you're overqualified for your current job.)

In other words, \ ``orig``\  is mapped onto (surjectively) \ ``dst``\ ,
using the map { <n, m> \| the n-th bit of \ ``relmap``\  is the
m-th set bit of \ ``relmap``\  }.

Any set bits in \ ``orig``\  above bit number W, where W is the
weight of (number of set bits in) \ ``relmap``\  are mapped nowhere.
In particular, if for all bits m set in \ ``orig``\ , m >= W, then
\ ``dst``\  will end up empty.  In situations where the possibility
of such an empty result is not desired, one way to avoid it is
to use the \ :c:func:`bitmap_fold`\  operator, below, to first fold the
\ ``orig``\  bitmap over itself so that all its set bits x are in the
range 0 <= x < W.  The \ :c:func:`bitmap_fold`\  operator does this by
setting the bit (m % W) in \ ``dst``\ , for each bit (m) set in \ ``orig``\ .

Example [1] for \ :c:func:`bitmap_onto`\ :
Let's say \ ``relmap``\  has bits 30-39 set, and \ ``orig``\  has bits
1, 3, 5, 7, 9 and 11 set.  Then on return from this routine,
\ ``dst``\  will have bits 31, 33, 35, 37 and 39 set.

When bit 0 is set in \ ``orig``\ , it means turn on the bit in
\ ``dst``\  corresponding to whatever is the first bit (if any)
that is turned on in \ ``relmap``\ .  Since bit 0 was off in the
above example, we leave off that bit (bit 30) in \ ``dst``\ .

When bit 1 is set in \ ``orig``\  (as in the above example), it
means turn on the bit in \ ``dst``\  corresponding to whatever
is the second bit that is turned on in \ ``relmap``\ .  The second
bit in \ ``relmap``\  that was turned on in the above example was
bit 31, so we turned on bit 31 in \ ``dst``\ .

Similarly, we turned on bits 33, 35, 37 and 39 in \ ``dst``\ ,
because they were the 4th, 6th, 8th and 10th set bits
set in \ ``relmap``\ , and the 4th, 6th, 8th and 10th bits of
\ ``orig``\  (i.e. bits 3, 5, 7 and 9) were also set.

When bit 11 is set in \ ``orig``\ , it means turn on the bit in
\ ``dst``\  corresponding to whatever is the twelfth bit that is
turned on in \ ``relmap``\ .  In the above example, there were
only ten bits turned on in \ ``relmap``\  (30..39), so that bit
11 was set in \ ``orig``\  had no affect on \ ``dst``\ .

Example [2] for \ :c:func:`bitmap_fold`\  + \ :c:func:`bitmap_onto`\ :
Let's say \ ``relmap``\  has these ten bits set:
40 41 42 43 45 48 53 61 74 95
(for the curious, that's 40 plus the first ten terms of the
Fibonacci sequence.)

Further lets say we use the following code, invoking
\ :c:func:`bitmap_fold`\  then bitmap_onto, as suggested above to
avoid the possibility of an empty \ ``dst``\  result:

unsigned long \*tmp;     // a temporary bitmap's bits

bitmap_fold(tmp, orig, bitmap_weight(relmap, bits), bits);
bitmap_onto(dst, tmp, relmap, bits);

Then this table shows what various values of \ ``dst``\  would be, for
various \ ``orig``\ 's.  I list the zero-based positions of each set bit.
The tmp column shows the intermediate result, as computed by
using \ :c:func:`bitmap_fold`\  to fold the \ ``orig``\  bitmap modulo ten
(the weight of \ ``relmap``\ ).

\ ``orig``\            tmp            \ ``dst``\ 
0                0             40
1                1             41
9                9             95
10               0             40 (\*)
1 3 5 7          1 3 5 7       41 43 48 61
0 1 2 3 4        0 1 2 3 4     40 41 42 43 45
0 9 18 27        0 9 8 7       40 61 74 95
0 10 20 30       0             40
0 11 22 33       0 1 2 3       40 41 42 43
0 12 24 36       0 2 4 6       40 42 45 53
78 102 211       1 2 8         41 42 74 (\*)

(\*) For these marked lines, if we hadn't first done \ :c:func:`bitmap_fold`\ 
into tmp, then the \ ``dst``\  result would have been empty.

If either of \ ``orig``\  or \ ``relmap``\  is empty (no set bits), then \ ``dst``\ 
will be returned empty.

If (as explained above) the only set bits in \ ``orig``\  are in positions
m where m >= W, (where W is the weight of \ ``relmap``\ ) then \ ``dst``\  will
once again be returned empty.

All bits in \ ``dst``\  not set by the above rule are cleared.

.. _`bitmap_fold`:

bitmap_fold
===========

.. c:function:: void bitmap_fold(unsigned long *dst, const unsigned long *orig, unsigned int sz, unsigned int nbits)

    fold larger bitmap into smaller, modulo specified size

    :param unsigned long \*dst:
        resulting smaller bitmap

    :param const unsigned long \*orig:
        original larger bitmap

    :param unsigned int sz:
        specified size

    :param unsigned int nbits:
        number of bits in each of these bitmaps

.. _`bitmap_fold.description`:

Description
-----------

For each bit oldbit in \ ``orig``\ , set bit oldbit mod \ ``sz``\  in \ ``dst``\ .
Clear all other bits in \ ``dst``\ .  See further the comment and
Example [2] for \ :c:func:`bitmap_onto`\  for why and how to use this.

.. _`bitmap_find_free_region`:

bitmap_find_free_region
=======================

.. c:function:: int bitmap_find_free_region(unsigned long *bitmap, unsigned int bits, int order)

    find a contiguous aligned mem region

    :param unsigned long \*bitmap:
        array of unsigned longs corresponding to the bitmap

    :param unsigned int bits:
        number of bits in the bitmap

    :param int order:
        region size (log base 2 of number of bits) to find

.. _`bitmap_find_free_region.description`:

Description
-----------

Find a region of free (zero) bits in a \ ``bitmap``\  of \ ``bits``\  bits and
allocate them (set them to one).  Only consider regions of length
a power (@order) of two, aligned to that power of two, which
makes the search algorithm much faster.

Return the bit offset in bitmap of the allocated region,
or -errno on failure.

.. _`bitmap_release_region`:

bitmap_release_region
=====================

.. c:function:: void bitmap_release_region(unsigned long *bitmap, unsigned int pos, int order)

    release allocated bitmap region

    :param unsigned long \*bitmap:
        array of unsigned longs corresponding to the bitmap

    :param unsigned int pos:
        beginning of bit region to release

    :param int order:
        region size (log base 2 of number of bits) to release

.. _`bitmap_release_region.description`:

Description
-----------

This is the complement to \__bitmap_find_free_region() and releases
the found region (by clearing it in the bitmap).

No return value.

.. _`bitmap_allocate_region`:

bitmap_allocate_region
======================

.. c:function:: int bitmap_allocate_region(unsigned long *bitmap, unsigned int pos, int order)

    allocate bitmap region

    :param unsigned long \*bitmap:
        array of unsigned longs corresponding to the bitmap

    :param unsigned int pos:
        beginning of bit region to allocate

    :param int order:
        region size (log base 2 of number of bits) to allocate

.. _`bitmap_allocate_region.description`:

Description
-----------

Allocate (set bits in) a specified region of a bitmap.

Return 0 on success, or \ ``-EBUSY``\  if specified region wasn't
free (not all bits were zero).

.. _`bitmap_from_u32array`:

bitmap_from_u32array
====================

.. c:function:: unsigned int bitmap_from_u32array(unsigned long *bitmap, unsigned int nbits, const u32 *buf, unsigned int nwords)

    copy the contents of a u32 array of bits to bitmap

    :param unsigned long \*bitmap:
        array of unsigned longs, the destination bitmap, non NULL

    :param unsigned int nbits:
        number of bits in \ ``bitmap``\ 

    :param const u32 \*buf:
        array of u32 (in host byte order), the source bitmap, non NULL

    :param unsigned int nwords:
        number of u32 words in \ ``buf``\ 

.. _`bitmap_from_u32array.description`:

Description
-----------

copy min(nbits, 32\*nwords) bits from \ ``buf``\  to \ ``bitmap``\ , remaining
bits between nword and nbits in \ ``bitmap``\  (if any) are cleared. In
last word of \ ``bitmap``\ , the bits beyond nbits (if any) are kept
unchanged.

Return the number of bits effectively copied.

.. _`bitmap_to_u32array`:

bitmap_to_u32array
==================

.. c:function:: unsigned int bitmap_to_u32array(u32 *buf, unsigned int nwords, const unsigned long *bitmap, unsigned int nbits)

    copy the contents of bitmap to a u32 array of bits

    :param u32 \*buf:
        array of u32 (in host byte order), the dest bitmap, non NULL

    :param unsigned int nwords:
        number of u32 words in \ ``buf``\ 

    :param const unsigned long \*bitmap:
        array of unsigned longs, the source bitmap, non NULL

    :param unsigned int nbits:
        number of bits in \ ``bitmap``\ 

.. _`bitmap_to_u32array.description`:

Description
-----------

copy min(nbits, 32\*nwords) bits from \ ``bitmap``\  to \ ``buf``\ . Remaining
bits after nbits in \ ``buf``\  (if any) are cleared.

Return the number of bits effectively copied.

.. _`bitmap_copy_le`:

bitmap_copy_le
==============

.. c:function:: void bitmap_copy_le(unsigned long *dst, const unsigned long *src, unsigned int nbits)

    copy a bitmap, putting the bits into little-endian order.

    :param unsigned long \*dst:
        destination buffer

    :param const unsigned long \*src:
        bitmap to copy

    :param unsigned int nbits:
        number of bits in the bitmap

.. _`bitmap_copy_le.description`:

Description
-----------

Require nbits % BITS_PER_LONG == 0.

.. This file was automatic generated / don't edit.

