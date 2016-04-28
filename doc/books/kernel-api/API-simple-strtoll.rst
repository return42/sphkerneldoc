.. -*- coding: utf-8; mode: rst -*-

.. _API-simple-strtoll:

==============
simple_strtoll
==============

*man simple_strtoll(9)*

*4.6.0-rc5*

convert a string to a signed long long


Synopsis
========

.. c:function:: long long simple_strtoll( const char * cp, char ** endp, unsigned int base )

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

This function is obsolete. Please use kstrtoll instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
