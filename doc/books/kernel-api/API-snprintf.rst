
.. _API-snprintf:

========
snprintf
========

*man snprintf(9)*

*4.6.0-rc1*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int snprintf( char * buf, size_t size, const char * fmt, ... )

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

The return value is the number of characters which would be generated for the given input, excluding the trailing null, as per ISO C99. If the return is greater than or equal to
``size``, the resulting string is truncated.

See the ``vsnprintf`` documentation for format string extensions over C99.
