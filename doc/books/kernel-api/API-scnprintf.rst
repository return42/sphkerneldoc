
.. _API-scnprintf:

=========
scnprintf
=========

*man scnprintf(9)*

*4.6.0-rc1*

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

The return value is the number of characters written into ``buf`` not including the trailing '\\0'. If ``size`` is == 0 the function returns 0.
