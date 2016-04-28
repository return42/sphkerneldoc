.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-copy-le:

==============
bitmap_copy_le
==============

*man bitmap_copy_le(9)*

*4.6.0-rc5*

copy a bitmap, putting the bits into little-endian order.


Synopsis
========

.. c:function:: void bitmap_copy_le( unsigned long * dst, const unsigned long * src, unsigned int nbits )

Arguments
=========

``dst``
    destination buffer

``src``
    bitmap to copy

``nbits``
    number of bits in the bitmap


Description
===========

Require nbits % BITS_PER_LONG == 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
