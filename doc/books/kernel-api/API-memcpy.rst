.. -*- coding: utf-8; mode: rst -*-

.. _API-memcpy:

======
memcpy
======

*man memcpy(9)*

*4.6.0-rc5*

Copy one area of memory to another


Synopsis
========

.. c:function:: void * memcpy( void * dest, const void * src, size_t count )

Arguments
=========

``dest``
    Where to copy to

``src``
    Where to copy from

``count``
    The size of the area.


Description
===========

You should not use this function to access IO space, use ``memcpy_toio``
or ``memcpy_fromio`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
