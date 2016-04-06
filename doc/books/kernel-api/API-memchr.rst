
.. _API-memchr:

======
memchr
======

*man memchr(9)*

*4.6.0-rc1*

Find a character in an area of memory.


Synopsis
========

.. c:function:: void ⋆ memchr( const void * s, int c, size_t n )

Arguments
=========

``s``
    The memory area

``c``
    The byte to search for

``n``
    The size of the area.


Description
===========

returns the address of the first occurrence of ``c``, or ``NULL`` if ``c`` is not found
