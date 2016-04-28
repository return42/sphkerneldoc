.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-from-u32array:

====================
bitmap_from_u32array
====================

*man bitmap_from_u32array(9)*

*4.6.0-rc5*

copy the contents of a u32 array of bits to bitmap


Synopsis
========

.. c:function:: unsigned int bitmap_from_u32array( unsigned long * bitmap, unsigned int nbits, const u32 * buf, unsigned int nwords )

Arguments
=========

``bitmap``
    array of unsigned longs, the destination bitmap, non NULL

``nbits``
    number of bits in ``bitmap``

``buf``
    array of u32 (in host byte order), the source bitmap, non NULL

``nwords``
    number of u32 words in ``buf``


Description
===========

copy min(nbits, 32*nwords) bits from ``buf`` to ``bitmap``, remaining
bits between nword and nbits in ``bitmap`` (if any) are cleared. In last
word of ``bitmap``, the bits beyond nbits (if any) are kept unchanged.

Return the number of bits effectively copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
