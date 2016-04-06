
.. _API---bitmap-parse:

==============
__bitmap_parse
==============

*man __bitmap_parse(9)*

*4.6.0-rc1*

convert an ASCII hex string into a bitmap.


Synopsis
========

.. c:function:: int __bitmap_parse( const char * buf, unsigned int buflen, int is_user, unsigned long * maskp, int nmaskbits )

Arguments
=========

``buf``
    pointer to buffer containing string.

``buflen``
    buffer size in bytes. If string is smaller than this then it must be terminated with a \\0.

``is_user``
    location of buffer, 0 indicates kernel space

``maskp``
    pointer to bitmap array that will contain result.

``nmaskbits``
    size of bitmap, in bits.


Description
===========

Commas group hex digits into chunks. Each chunk defines exactly 32 bits of the resultant bitmask. No chunk may specify a value larger than 32 bits (``-EOVERFLOW``), and if a chunk
specifies a smaller value then leading 0-bits are prepended. ``-EINVAL`` is returned for illegal characters and for grouping errors such as “1,,5”, “,44”, “,” and "". Leading and
trailing whitespace accepted, but not embedded whitespace.
