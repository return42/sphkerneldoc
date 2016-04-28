.. -*- coding: utf-8; mode: rst -*-

.. _API---bitmap-shift-right:

====================
__bitmap_shift_right
====================

*man __bitmap_shift_right(9)*

*4.6.0-rc5*

logical right shift of the bits in a bitmap


Synopsis
========

.. c:function:: void __bitmap_shift_right( unsigned long * dst, const unsigned long * src, unsigned shift, unsigned nbits )

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

Shifting right (dividing) means moving bits in the MS -> LS bit
direction. Zeros are fed into the vacated MS positions and the LS bits
shifted off the bottom are lost.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
