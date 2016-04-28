.. -*- coding: utf-8; mode: rst -*-

.. _API-fls64:

=====
fls64
=====

*man fls64(9)*

*4.6.0-rc5*

find last set bit in a 64-bit word


Synopsis
========

.. c:function:: int fls64( __u64 x )

Arguments
=========

``x``
    the word to search


Description
===========

This is defined in a similar way as the libc and compiler builtin ffsll,
but returns the position of the most significant set bit.

fls64(value) returns 0 if value is 0 or the position of the last set bit
if value is nonzero. The last (most significant) bit is at position 64.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
