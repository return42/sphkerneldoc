
.. _API-bitmap-bitremap:

===============
bitmap_bitremap
===============

*man bitmap_bitremap(9)*

*4.6.0-rc1*

Apply map defined by a pair of bitmaps to a single bit


Synopsis
========

.. c:function:: int bitmap_bitremap( int oldbit, const unsigned long * old, const unsigned long * new, int bits )

Arguments
=========

``oldbit``
    bit position to be mapped

``old``
    defines domain of map

``new``
    defines range of map

``bits``
    number of bits in each of these bitmaps


Description
===========

Let ``old`` and ``new`` define a mapping of bit positions, such that whatever position is held by the n-th set bit in ``old`` is mapped to the n-th set bit in ``new``. In the more
general case, allowing for the possibility that the weight 'w' of ``new`` is less than the weight of ``old``, map the position of the n-th set bit in ``old`` to the position of the
m-th set bit in ``new``, where m == n % w.

The positions of unset bits in ``old`` are mapped to themselves (the identify map).

Apply the above specified mapping to bit position ``oldbit``, returning the new bit position.

For example, lets say that ``old`` has bits 4 through 7 set, and ``new`` has bits 12 through 15 set. This defines the mapping of bit position 4 to 12, 5 to 13, 6 to 14 and 7 to 15,
and of all other bit positions unchanged. So if say ``oldbit`` is 5, then this routine returns 13.
