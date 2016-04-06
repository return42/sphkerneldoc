
.. _API-bitmap-pos-to-ord:

=================
bitmap_pos_to_ord
=================

*man bitmap_pos_to_ord(9)*

*4.6.0-rc1*

find ordinal of set bit at given position in bitmap


Synopsis
========

.. c:function:: int bitmap_pos_to_ord( const unsigned long * buf, unsigned int pos, unsigned int nbits )

Arguments
=========

``buf``
    pointer to a bitmap

``pos``
    a bit position in ``buf`` (0 <= ``pos`` < ``nbits``)

``nbits``
    number of valid bit positions in ``buf``


Description
===========

Map the bit at position ``pos`` in ``buf`` (of length ``nbits``) to the ordinal of which set bit it is. If it is not set or if ``pos`` is not a valid bit position, map to -1.

If for example, just bits 4 through 7 are set in ``buf``, then ``pos`` values 4 through 7 will get mapped to 0 through 3, respectively, and other ``pos`` values will get mapped to
-1. When ``pos`` value 7 gets mapped to (returns) ``ord`` value 3 in this example, that means that bit 7 is the 3rd (starting with 0th) set bit in ``buf``.

The bit positions 0 through ``bits`` are valid positions in ``buf``.
