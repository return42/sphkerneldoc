.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-to-u32array:

==================
bitmap_to_u32array
==================

*man bitmap_to_u32array(9)*

*4.6.0-rc5*

copy the contents of bitmap to a u32 array of bits


Synopsis
========

.. c:function:: unsigned int bitmap_to_u32array( u32 * buf, unsigned int nwords, const unsigned long * bitmap, unsigned int nbits )

Arguments
=========

``buf``
    array of u32 (in host byte order), the dest bitmap, non NULL

``nwords``
    number of u32 words in ``buf``

``bitmap``
    array of unsigned longs, the source bitmap, non NULL

``nbits``
    number of bits in ``bitmap``


Description
===========

copy min(nbits, 32*nwords) bits from ``bitmap`` to ``buf``. Remaining
bits after nbits in ``buf`` (if any) are cleared.

Return the number of bits effectively copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
