
.. _API-mpt-reset-deregister:

====================
mpt_reset_deregister
====================

*man mpt_reset_deregister(9)*

*4.6.0-rc1*

Deregister protocol-specific IOC reset handler.


Synopsis
========

.. c:function:: void mpt_reset_deregister( u8 cb_idx )

Arguments
=========

``cb_idx``
    previously registered callback handle


Description
===========

Each protocol-specific driver should call this routine when it does not (or can no longer) handle IOC reset handling, or when its module is unloaded.
