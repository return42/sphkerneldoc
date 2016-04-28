.. -*- coding: utf-8; mode: rst -*-

.. _API-upper-32-bits:

=============
upper_32_bits
=============

*man upper_32_bits(9)*

*4.6.0-rc5*

return bits 32-63 of a number


Synopsis
========

.. c:function:: upper_32_bits( n )

Arguments
=========

``n``
    the number we're accessing


Description
===========

A basic shift-right of a 64- or 32-bit quantity. Use this to suppress
the “right shift count >= width of type” warning when that quantity is
32-bits.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
