.. -*- coding: utf-8; mode: rst -*-

.. _API-ida-simple-get:

==============
ida_simple_get
==============

*man ida_simple_get(9)*

*4.6.0-rc5*

get a new id.


Synopsis
========

.. c:function:: int ida_simple_get( struct ida * ida, unsigned int start, unsigned int end, gfp_t gfp_mask )

Arguments
=========

``ida``
    the (initialized) ida.

``start``
    the minimum id (inclusive, < 0x8000000)

``end``
    the maximum id (exclusive, < 0x8000000 or 0)

``gfp_mask``
    memory allocation flags


Description
===========

Allocates an id in the range start <= id < end, or returns -ENOSPC. On
memory allocation failure, returns -ENOMEM.

Use ``ida_simple_remove`` to get rid of an id.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
