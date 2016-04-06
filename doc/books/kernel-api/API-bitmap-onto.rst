
.. _API-bitmap-onto:

===========
bitmap_onto
===========

*man bitmap_onto(9)*

*4.6.0-rc1*

translate one bitmap relative to another


Synopsis
========

.. c:function:: void bitmap_onto( unsigned long * dst, const unsigned long * orig, const unsigned long * relmap, unsigned int bits )

Arguments
=========

``dst``
    resulting translated bitmap

``orig``
    original untranslated bitmap

``relmap``
    bitmap relative to which translated

``bits``
    number of bits in each of these bitmaps


Description
===========

Set the n-th bit of ``dst`` iff there exists some m such that the n-th bit of ``relmap`` is set, the m-th bit of ``orig`` is set, and the n-th bit of ``relmap`` is also the m-th
_set_ bit of ``relmap``. (If you understood the previous sentence the first time your read it, you're overqualified for your current job.)

In other words, ``orig`` is mapped onto (surjectively) ``dst``, using the map { <n, m> | the n-th bit of ``relmap`` is the m-th set bit of ``relmap`` }.

Any set bits in ``orig`` above bit number W, where W is the weight of (number of set bits in) ``relmap`` are mapped nowhere. In particular, if for all bits m set in ``orig``, m >=
W, then ``dst`` will end up empty. In situations where the possibility of such an empty result is not desired, one way to avoid it is to use the ``bitmap_fold`` operator, below, to
first fold the ``orig`` bitmap over itself so that all its set bits x are in the range 0 <= x < W. The ``bitmap_fold`` operator does this by setting the bit (m % W) in ``dst``, for
each bit (m) set in ``orig``.

Example [1] for ``bitmap_onto``: Let's say ``relmap`` has bits 30-39 set, and ``orig`` has bits 1, 3, 5, 7, 9 and 11 set. Then on return from this routine, ``dst`` will have bits
31, 33, 35, 37 and 39 set.

When bit 0 is set in ``orig``, it means turn on the bit in ``dst`` corresponding to whatever is the first bit (if any) that is turned on in ``relmap``. Since bit 0 was off in the
above example, we leave off that bit (bit 30) in ``dst``.

When bit 1 is set in ``orig`` (as in the above example), it means turn on the bit in ``dst`` corresponding to whatever is the second bit that is turned on in ``relmap``. The second
bit in ``relmap`` that was turned on in the above example was bit 31, so we turned on bit 31 in ``dst``.

Similarly, we turned on bits 33, 35, 37 and 39 in ``dst``, because they were the 4th, 6th, 8th and 10th set bits set in ``relmap``, and the 4th, 6th, 8th and 10th bits of ``orig``
(i.e. bits 3, 5, 7 and 9) were also set.

When bit 11 is set in ``orig``, it means turn on the bit in ``dst`` corresponding to whatever is the twelfth bit that is turned on in ``relmap``. In the above example, there were
only ten bits turned on in ``relmap`` (30..39), so that bit 11 was set in ``orig`` had no affect on ``dst``.

Example [2] for ``bitmap_fold`` + ``bitmap_onto``: Let's say ``relmap`` has these ten bits set: 40 41 42 43 45 48 53 61 74 95 (for the curious, that's 40 plus the first ten terms
of the Fibonacci sequence.)

Further lets say we use the following code, invoking ``bitmap_fold`` then bitmap_onto, as suggested above to avoid the possibility of an empty ``dst`` result:

unsigned long ⋆tmp; // a temporary bitmap's bits

bitmap_fold(tmp, orig, bitmap_weight(relmap, bits), bits); bitmap_onto(dst, tmp, relmap, bits);

Then this table shows what various values of ``dst`` would be, for various ``orig``'s. I list the zero-based positions of each set bit. The tmp column shows the intermediate
result, as computed by using ``bitmap_fold`` to fold the ``orig`` bitmap modulo ten (the weight of ``relmap``).

``orig`` tmp ``dst`` 0 0 40 1 1 41 9 9 95 10 0 40 (⋆) 1 3 5 7 1 3 5 7 41 43 48 61 0 1 2 3 4 0 1 2 3 4 40 41 42 43 45 0 9 18 27 0 9 8 7 40 61 74 95 0 10 20 30 0 40 0 11 22 33 0 1 2
3 40 41 42 43 0 12 24 36 0 2 4 6 40 42 45 53 78 102 211 1 2 8 41 42 74 (⋆)

(⋆) For these marked lines, if we hadn't first done ``bitmap_fold`` into tmp, then the ``dst`` result would have been empty.

If either of ``orig`` or ``relmap`` is empty (no set bits), then ``dst`` will be returned empty.

If (as explained above) the only set bits in ``orig`` are in positions m where m >= W, (where W is the weight of ``relmap``) then ``dst`` will once again be returned empty.

All bits in ``dst`` not set by the above rule are cleared.
