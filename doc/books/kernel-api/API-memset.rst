.. -*- coding: utf-8; mode: rst -*-

.. _API-memset:

======
memset
======

*man memset(9)*

*4.6.0-rc5*

Fill a region of memory with the given value


Synopsis
========

.. c:function:: void * memset( void * s, int c, size_t count )

Arguments
=========

``s``
    Pointer to the start of the area.

``c``
    The byte to fill the area with

``count``
    The size of the area.


Description
===========

Do not use ``memset`` to access IO space, use ``memset_io`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
