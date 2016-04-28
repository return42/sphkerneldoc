.. -*- coding: utf-8; mode: rst -*-

.. _API-fls:

===
fls
===

*man fls(9)*

*4.6.0-rc5*

find last set bit in word


Synopsis
========

.. c:function:: int fls( int x )

Arguments
=========

``x``
    the word to search


Description
===========

This is defined in a similar way as the libc and compiler builtin ffs,
but returns the position of the most significant set bit.

fls(value) returns 0 if value is 0 or the position of the last set bit
if value is nonzero. The last (most significant) bit is at position 32.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
