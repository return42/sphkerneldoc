.. -*- coding: utf-8; mode: rst -*-

.. _API-change-bit:

==========
change_bit
==========

*man change_bit(9)*

*4.6.0-rc5*

Toggle a bit in memory


Synopsis
========

.. c:function:: void change_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to change

``addr``
    Address to start counting from


Description
===========

``change_bit`` is atomic and may not be reordered. Note that ``nr`` may
be almost arbitrarily large; this function is not restricted to acting
on a single-word quantity.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
