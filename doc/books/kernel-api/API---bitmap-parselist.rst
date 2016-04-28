.. -*- coding: utf-8; mode: rst -*-

.. _API---bitmap-parselist:

==================
__bitmap_parselist
==================

*man __bitmap_parselist(9)*

*4.6.0-rc5*

convert list format ASCII string to bitmap


Synopsis
========

.. c:function:: int __bitmap_parselist( const char * buf, unsigned int buflen, int is_user, unsigned long * maskp, int nmaskbits )

Arguments
=========

``buf``
    read nul-terminated user string from this buffer

``buflen``
    buffer size in bytes. If string is smaller than this then it must be
    terminated with a \\0.

``is_user``
    location of buffer, 0 indicates kernel space

``maskp``
    write resulting mask here

``nmaskbits``
    number of bits in mask to be written


Description
===========

Input format is a comma-separated list of decimal numbers and ranges.
Consecutively set bits are shown as two hyphen-separated decimal
numbers, the smallest and largest bit numbers set in the range.

Returns 0 on success, -errno on invalid input strings.


Error values
============

``-EINVAL``: second number in range smaller than first ``-EINVAL``:
invalid character in string ``-ERANGE``: bit number specified too large
for mask


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
