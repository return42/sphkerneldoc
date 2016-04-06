
.. _API-bprintf:

=======
bprintf
=======

*man bprintf(9)*

*4.6.0-rc1*

Parse a format string and place args' binary value in a buffer


Synopsis
========

.. c:function:: int bprintf( u32 * bin_buf, size_t size, const char * fmt, ... )

Arguments
=========

``bin_buf``
    The buffer to place args' binary value

``size``
    The size of the buffer(by words(32bits), not characters)

``fmt``
    The format string to use @...: Arguments for the format string

``...``
    variable arguments


Description
===========

The function returns the number of words(u32) written into ``bin_buf``.
