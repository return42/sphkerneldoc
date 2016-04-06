
.. _API-mpt-deregister:

==============
mpt_deregister
==============

*man mpt_deregister(9)*

*4.6.0-rc1*

Deregister a protocol drivers resources.


Synopsis
========

.. c:function:: void mpt_deregister( u8 cb_idx )

Arguments
=========

``cb_idx``
    previously registered callback handle


Description
===========

Each protocol-specific driver should call this routine when its module is unloaded.
