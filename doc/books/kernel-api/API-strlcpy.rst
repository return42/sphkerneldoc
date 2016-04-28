.. -*- coding: utf-8; mode: rst -*-

.. _API-strlcpy:

=======
strlcpy
=======

*man strlcpy(9)*

*4.6.0-rc5*

Copy a C-string into a sized buffer


Synopsis
========

.. c:function:: size_t strlcpy( char * dest, const char * src, size_t size )

Arguments
=========

``dest``
    Where to copy the string to

``src``
    Where to copy the string from

``size``
    size of destination buffer


BSD
===

the result is always a valid NUL-terminated string that fits in the
buffer (unless, of course, the buffer size is zero). It does not pad out
the result like ``strncpy`` does.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
