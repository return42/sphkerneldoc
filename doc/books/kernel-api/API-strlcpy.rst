
.. _API-strlcpy:

=======
strlcpy
=======

*man strlcpy(9)*

*4.6.0-rc1*

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

the result is always a valid NUL-terminated string that fits in the buffer (unless, of course, the buffer size is zero). It does not pad out the result like ``strncpy`` does.
