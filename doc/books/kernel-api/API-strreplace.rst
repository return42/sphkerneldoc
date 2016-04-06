
.. _API-strreplace:

==========
strreplace
==========

*man strreplace(9)*

*4.6.0-rc1*

Replace all occurrences of character in string.


Synopsis
========

.. c:function:: char ⋆ strreplace( char * s, char old, char new )

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
