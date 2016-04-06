
.. _API-bitmap-remap:

============
bitmap_remap
============

*man bitmap_remap(9)*

*4.6.0-rc1*

Apply map defined by a pair of bitmaps to another bitmap


Synopsis
========

.. c:function:: void bitmap_remap( unsigned long * dst, const unsigned long * src, const unsigned long * old, const unsigned long * new, unsigned int nbits )

Arguments
=========

``dst``
    remapped result

``src``
    subset to be remapped

``old``
    defines domain of map

``new``
    defines range of map

``nbits``
    number of bits in each of these bitmaps


Description
===========

Let ``old`` and ``new`` define a mapping of bit positions, such that whatever position is held by the n-th set bit in ``old`` is mapped to the n-th set bit in ``new``. In the more
general case, allowing for the possibility that the weight 'w' of ``new`` is less than the weight of ``old``, map the position of the n-th set bit in ``old`` to the position of the
m-th set bit in ``new``, where m == n % w.

If either of the ``old`` and ``new`` bitmaps are empty, or if ``src`` and ``dst`` point to the same location, then this routine copies ``src`` to ``dst``.

The positions of unset bits in ``old`` are mapped to themselves (the identify map).

Apply the above specified mapping to ``src``, placing the result in ``dst``, clearing any bits previously set in ``dst``.

For example, lets say that ``old`` has bits 4 through 7 set, and ``new`` has bits 12 through 15 set. This defines the mapping of bit position 4 to 12, 5 to 13, 6 to 14 and 7 to 15,
and of all other bit positions unchanged. So if say ``src`` comes into this routine with bits 1, 5 and 7 set, then ``dst`` should leave with bits 1, 13 and 15 set.
