
.. _API-mpt-event-deregister:

====================
mpt_event_deregister
====================

*man mpt_event_deregister(9)*

*4.6.0-rc1*

Deregister protocol-specific event callback handler


Synopsis
========

.. c:function:: void mpt_event_deregister( u8 cb_idx )

Arguments
=========

``cb_idx``
    previously registered callback handle


Description
===========

Each protocol-specific driver should call this routine when it does not (or can no longer) handle events, or when its module is unloaded.
