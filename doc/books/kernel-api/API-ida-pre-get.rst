.. -*- coding: utf-8; mode: rst -*-

.. _API-ida-pre-get:

===========
ida_pre_get
===========

*man ida_pre_get(9)*

*4.6.0-rc5*

reserve resources for ida allocation


Synopsis
========

.. c:function:: int ida_pre_get( struct ida * ida, gfp_t gfp_mask )

Arguments
=========

``ida``
    ida handle

``gfp_mask``
    memory allocation flag


Description
===========

This function should be called prior to locking and calling the
following function. It preallocates enough memory to satisfy the worst
possible allocation.

If the system is REALLY out of memory this function returns ``0``,
otherwise ``1``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
