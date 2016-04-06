
.. _API-vbin-printf:

===========
vbin_printf
===========

*man vbin_printf(9)*

*4.6.0-rc1*

Parse a format string and place args' binary value in a buffer


Synopsis
========

.. c:function:: int vbin_printf( u32 * bin_buf, size_t size, const char * fmt, va_list args )

Arguments
=========

``bin_buf``
    The buffer to place args' binary value

``size``
    The size of the buffer(by words(32bits), not characters)

``fmt``
    The format string to use

``args``
    Arguments for the format string


Description
===========

The format follows C99 vsnprintf, except ``n`` is ignored, and its argument is skipped.

The return value is the number of words(32bits) which would be generated for the given input.


NOTE
====

If the return value is greater than ``size``, the resulting bin_buf is NOT valid for ``bstr_printf``.
