.. -*- coding: utf-8; mode: rst -*-

.. _API---bitmap-shift-left:

===================
__bitmap_shift_left
===================

*man __bitmap_shift_left(9)*

*4.6.0-rc5*

logical left shift of the bits in a bitmap


Synopsis
========

.. c:function:: void __bitmap_shift_left( unsigned long * dst, const unsigned long * src, unsigned int shift, unsigned int nbits )

Arguments
=========

``dst``
    destination bitmap

``src``
    source bitmap

``shift``
    shift by this many bits

``nbits``
    bitmap size, in bits


Description
===========

Shifting left (multiplying) means moving bits in the LS -> MS direction.
Zeros are fed into the vacated LS bit positions and those MS bits
shifted off the top are lost.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
