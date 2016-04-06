
.. _API-skip-spaces:

===========
skip_spaces
===========

*man skip_spaces(9)*

*4.6.0-rc1*

Removes leading whitespace from ``str``.


Synopsis
========

.. c:function:: char ⋆ skip_spaces( const char * str )

Arguments
=========

``str``
    The string to be stripped.


Description
===========

Returns a pointer to the first non-whitespace character in ``str``.
