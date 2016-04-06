
.. _API-strchrnul:

=========
strchrnul
=========

*man strchrnul(9)*

*4.6.0-rc1*

Find and return a character in a string, or end of string


Synopsis
========

.. c:function:: char ⋆ strchrnul( const char * s, int c )

Arguments
=========

``s``
    The string to be searched

``c``
    The character to search for


Description
===========

Returns pointer to first occurrence of 'c' in s. If c is not found, then return a pointer to the null byte at the end of s.
