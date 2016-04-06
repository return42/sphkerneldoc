
.. _API-simple-strtoul:

==============
simple_strtoul
==============

*man simple_strtoul(9)*

*4.6.0-rc1*

convert a string to an unsigned long


Synopsis
========

.. c:function:: unsigned long simple_strtoul( const char * cp, char ** endp, unsigned int base )

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

This function is obsolete. Please use kstrtoul instead.
