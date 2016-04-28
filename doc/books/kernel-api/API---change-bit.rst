.. -*- coding: utf-8; mode: rst -*-

.. _API---change-bit:

============
__change_bit
============

*man __change_bit(9)*

*4.6.0-rc5*

Toggle a bit in memory


Synopsis
========

.. c:function:: void __change_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    the bit to change

``addr``
    the address to start counting from


Description
===========

Unlike ``change_bit``, this function is non-atomic and may be reordered.
If it's called on the same region of memory simultaneously, the effect
may be that only one operation succeeds.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
