.. -*- coding: utf-8; mode: rst -*-

.. _API-memchr:

======
memchr
======

*man memchr(9)*

*4.6.0-rc5*

Find a character in an area of memory.


Synopsis
========

.. c:function:: void * memchr( const void * s, int c, size_t n )

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

returns the address of the first occurrence of ``c``, or ``NULL`` if
``c`` is not found


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
