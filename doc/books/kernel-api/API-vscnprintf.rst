
.. _API-vscnprintf:

==========
vscnprintf
==========

*man vscnprintf(9)*

*4.6.0-rc1*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int vscnprintf( char * buf, size_t size, const char * fmt, va_list args )

Arguments
=========

``buf``
    The buffer to place the result into

``size``
    The size of the buffer, including the trailing null space

``fmt``
    The format string to use

``args``
    Arguments for the format string


Description
===========

The return value is the number of characters which have been written into the ``buf`` not including the trailing '\\0'. If ``size`` is == 0 the function returns 0.

If you're not already dealing with a va_list consider using ``scnprintf``.

See the ``vsnprintf`` documentation for format string extensions over C99.
