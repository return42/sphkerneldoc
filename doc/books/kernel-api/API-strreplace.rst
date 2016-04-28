.. -*- coding: utf-8; mode: rst -*-

.. _API-strreplace:

==========
strreplace
==========

*man strreplace(9)*

*4.6.0-rc5*

Replace all occurrences of character in string.


Synopsis
========

.. c:function:: char * strreplace( char * s, char old, char new )

Arguments
=========

``s``
    The string to operate on.

``old``
    The character being replaced.

``new``
    The character ``old`` is replaced with.


Description
===========

Returns pointer to the nul byte at the end of ``s``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
