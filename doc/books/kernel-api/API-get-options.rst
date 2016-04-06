
.. _API-get-options:

===========
get_options
===========

*man get_options(9)*

*4.6.0-rc1*

Parse a string into a list of integers


Synopsis
========

.. c:function:: char ⋆ get_options( const char * str, int nints, int * ints )

Arguments
=========

``str``
    String to be parsed

``nints``
    size of integer array

``ints``
    integer array


Description
===========

This function parses a string containing a comma-separated list of integers, a hyphen-separated range of _positive_ integers, or a combination of both. The parse halts when the
array is full, or when no more numbers can be retrieved from the string.

Return value is the character in the string which caused the parse to end (typically a null terminator, if ``str`` is completely parseable).
