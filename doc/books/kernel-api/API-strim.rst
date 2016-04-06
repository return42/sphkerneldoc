
.. _API-strim:

=====
strim
=====

*man strim(9)*

*4.6.0-rc1*

Removes leading and trailing whitespace from ``s``.


Synopsis
========

.. c:function:: char ⋆ strim( char * s )

Arguments
=========

``s``
    The string to be stripped.


Description
===========

Note that the first trailing whitespace is replaced with a ``NUL-terminator`` in the given string ``s``. Returns a pointer to the first non-whitespace character in ``s``.
