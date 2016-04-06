
.. _API-memchr-inv:

==========
memchr_inv
==========

*man memchr_inv(9)*

*4.6.0-rc1*

Find an unmatching character in an area of memory.


Synopsis
========

.. c:function:: void ⋆ memchr_inv( const void * start, int c, size_t bytes )

Arguments
=========

``start``
    The memory area

``c``
    Find a character other than c

``bytes``
    The size of the area.


Description
===========

returns the address of the first character other than ``c``, or ``NULL`` if the whole buffer contains just ``c``.
