.. -*- coding: utf-8; mode: rst -*-

.. _API-ffs:

===
ffs
===

*man ffs(9)*

*4.6.0-rc5*

find first set bit in word


Synopsis
========

.. c:function:: int ffs( int x )

Arguments
=========

``x``
    the word to search


Description
===========

This is defined the same way as the libc and compiler builtin ffs
routines, therefore differs in spirit from the other bitops.

ffs(value) returns 0 if value is 0 or the position of the first set bit
if value is nonzero. The first (least significant) bit is at position 1.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
