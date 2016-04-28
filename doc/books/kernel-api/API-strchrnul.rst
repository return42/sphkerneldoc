.. -*- coding: utf-8; mode: rst -*-

.. _API-strchrnul:

=========
strchrnul
=========

*man strchrnul(9)*

*4.6.0-rc5*

Find and return a character in a string, or end of string


Synopsis
========

.. c:function:: char * strchrnul( const char * s, int c )

Arguments
=========

``s``
    The string to be searched

``c``
    The character to search for


Description
===========

Returns pointer to first occurrence of 'c' in s. If c is not found, then
return a pointer to the null byte at the end of s.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
