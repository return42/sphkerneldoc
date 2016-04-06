
.. _API-bitmap-ord-to-pos:

=================
bitmap_ord_to_pos
=================

*man bitmap_ord_to_pos(9)*

*4.6.0-rc1*

find position of n-th set bit in bitmap


Synopsis
========

.. c:function:: unsigned int bitmap_ord_to_pos( const unsigned long * buf, unsigned int ord, unsigned int nbits )

Arguments
=========

``buf``
    pointer to bitmap

``ord``
    ordinal bit position (n-th set bit, n >= 0)

``nbits``
    number of valid bit positions in ``buf``


Description
===========

Map the ordinal offset of bit ``ord`` in ``buf`` to its position in ``buf``. Value of ``ord`` should be in range 0 <= ``ord`` < weight(buf). If ``ord`` >= weight(buf), returns
``nbits``.

If for example, just bits 4 through 7 are set in ``buf``, then ``ord`` values 0 through 3 will get mapped to 4 through 7, respectively, and all other ``ord`` values returns
``nbits``. When ``ord`` value 3 gets mapped to (returns) ``pos`` value 7 in this example, that means that the 3rd set bit (starting with 0th) is at position 7 in ``buf``.

The bit positions 0 through ``nbits``-1 are valid positions in ``buf``.
