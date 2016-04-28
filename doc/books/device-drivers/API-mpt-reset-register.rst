.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-reset-register:

==================
mpt_reset_register
==================

*man mpt_reset_register(9)*

*4.6.0-rc5*

Register protocol-specific IOC reset handler.


Synopsis
========

.. c:function:: int mpt_reset_register( u8 cb_idx, MPT_RESETHANDLER reset_func )

Arguments
=========

``cb_idx``
    previously registered (via mpt_register) callback handle

``reset_func``
    reset function


Description
===========

This routine can be called by one or more protocol-specific drivers
if/when they choose to be notified of IOC resets.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
