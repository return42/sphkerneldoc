
.. _API-mpt-reset-register:

==================
mpt_reset_register
==================

*man mpt_reset_register(9)*

*4.6.0-rc1*

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

This routine can be called by one or more protocol-specific drivers if/when they choose to be notified of IOC resets.

Returns 0 for success.
