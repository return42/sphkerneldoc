
.. _API-ffs:

===
ffs
===

*man ffs(9)*

*4.6.0-rc1*

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

This is defined the same way as the libc and compiler builtin ffs routines, therefore differs in spirit from the other bitops.

ffs(value) returns 0 if value is 0 or the position of the first set bit if value is nonzero. The first (least significant) bit is at position 1.
