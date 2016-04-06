
.. _API-memscan:

=======
memscan
=======

*man memscan(9)*

*4.6.0-rc1*

Find a character in an area of memory.


Synopsis
========

.. c:function:: void ⋆ memscan( void * addr, int c, size_t size )

Arguments
=========

``addr``
    The memory area

``c``
    The byte to search for

``size``
    The size of the area.


Description
===========

returns the address of the first occurrence of ``c``, or 1 byte past the area if ``c`` is not found
