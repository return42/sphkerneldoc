.. -*- coding: utf-8; mode: rst -*-

.. _API-get-options:

===========
get_options
===========

*man get_options(9)*

*4.6.0-rc5*

Parse a string into a list of integers


Synopsis
========

.. c:function:: char * get_options( const char * str, int nints, int * ints )

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

This function parses a string containing a comma-separated list of
integers, a hyphen-separated range of _positive_ integers, or a
combination of both. The parse halts when the array is full, or when no
more numbers can be retrieved from the string.

Return value is the character in the string which caused the parse to
end (typically a null terminator, if ``str`` is completely parseable).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
