.. -*- coding: utf-8; mode: rst -*-

.. _API-memchr-inv:

==========
memchr_inv
==========

*man memchr_inv(9)*

*4.6.0-rc5*

Find an unmatching character in an area of memory.


Synopsis
========

.. c:function:: void * memchr_inv( const void * start, int c, size_t bytes )

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

returns the address of the first character other than ``c``, or ``NULL``
if the whole buffer contains just ``c``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
