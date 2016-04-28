.. -*- coding: utf-8; mode: rst -*-

.. _API-scnprintf:

=========
scnprintf
=========

*man scnprintf(9)*

*4.6.0-rc5*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int scnprintf( char * buf, size_t size, const char * fmt, ... )

Arguments
=========

``buf``
    The buffer to place the result into

``size``
    The size of the buffer, including the trailing null space

``fmt``
    The format string to use @...: Arguments for the format string

``...``
    variable arguments


Description
===========

The return value is the number of characters written into ``buf`` not
including the trailing '\\0'. If ``size`` is == 0 the function returns
0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
