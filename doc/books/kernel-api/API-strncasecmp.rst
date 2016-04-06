
.. _API-strncasecmp:

===========
strncasecmp
===========

*man strncasecmp(9)*

*4.6.0-rc1*

Case insensitive, length-limited string comparison


Synopsis
========

.. c:function:: int strncasecmp( const char * s1, const char * s2, size_t len )

Arguments
=========

``s1``
    One string

``s2``
    The other string

``len``
    the maximum number of characters to compare
