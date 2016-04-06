
.. _API-bitmap-fold:

===========
bitmap_fold
===========

*man bitmap_fold(9)*

*4.6.0-rc1*

fold larger bitmap into smaller, modulo specified size


Synopsis
========

.. c:function:: void bitmap_fold( unsigned long * dst, const unsigned long * orig, unsigned int sz, unsigned int nbits )

Arguments
=========

``dst``
    resulting smaller bitmap

``orig``
    original larger bitmap

``sz``
    specified size

``nbits``
    number of bits in each of these bitmaps


Description
===========

For each bit oldbit in ``orig``, set bit oldbit mod ``sz`` in ``dst``. Clear all other bits in ``dst``. See further the comment and Example [2] for ``bitmap_onto`` for why and how
to use this.
