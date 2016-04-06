
.. _API-fls:

===
fls
===

*man fls(9)*

*4.6.0-rc1*

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

This is defined in a similar way as the libc and compiler builtin ffs, but returns the position of the most significant set bit.

fls(value) returns 0 if value is 0 or the position of the last set bit if value is nonzero. The last (most significant) bit is at position 32.
