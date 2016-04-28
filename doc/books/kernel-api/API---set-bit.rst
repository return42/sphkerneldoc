.. -*- coding: utf-8; mode: rst -*-

.. _API---set-bit:

=========
__set_bit
=========

*man __set_bit(9)*

*4.6.0-rc5*

Set a bit in memory


Synopsis
========

.. c:function:: void __set_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    the bit to set

``addr``
    the address to start counting from


Description
===========

Unlike ``set_bit``, this function is non-atomic and may be reordered. If
it's called on the same region of memory simultaneously, the effect may
be that only one operation succeeds.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
