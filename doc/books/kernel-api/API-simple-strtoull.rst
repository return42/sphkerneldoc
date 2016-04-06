
.. _API-simple-strtoull:

===============
simple_strtoull
===============

*man simple_strtoull(9)*

*4.6.0-rc1*

convert a string to an unsigned long long


Synopsis
========

.. c:function:: unsigned long long simple_strtoull( const char * cp, char ** endp, unsigned int base )

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

This function is obsolete. Please use kstrtoull instead.
