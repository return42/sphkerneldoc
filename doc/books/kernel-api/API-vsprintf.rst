
.. _API-vsprintf:

========
vsprintf
========

*man vsprintf(9)*

*4.6.0-rc1*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int vsprintf( char * buf, const char * fmt, va_list args )

Arguments
=========

``buf``
    The buffer to place the result into

``fmt``
    The format string to use

``args``
    Arguments for the format string


Description
===========

The function returns the number of characters written into ``buf``. Use ``vsnprintf`` or ``vscnprintf`` in order to avoid buffer overflows.

If you're not already dealing with a va_list consider using ``sprintf``.

See the ``vsnprintf`` documentation for format string extensions over C99.
