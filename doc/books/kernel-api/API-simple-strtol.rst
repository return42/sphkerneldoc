
.. _API-simple-strtol:

=============
simple_strtol
=============

*man simple_strtol(9)*

*4.6.0-rc1*

convert a string to a signed long


Synopsis
========

.. c:function:: long simple_strtol( const char * cp, char ** endp, unsigned int base )

Arguments
=========

``cp``
    The start of the string

``endp``
    A pointer to the end of the parsed string will be placed here

``base``
    The number base to use


Description
===========

This function is obsolete. Please use kstrtol instead.
