
.. _API-mpt-SoftResetHandler:

====================
mpt_SoftResetHandler
====================

*man mpt_SoftResetHandler(9)*

*4.6.0-rc1*

Issues a less expensive reset


Synopsis
========

.. c:function:: int mpt_SoftResetHandler( MPT_ADAPTER * ioc, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``sleepFlag``
    Indicates if sleep or schedule must be called.


Description
===========

Returns 0 for SUCCESS or -1 if FAILED.

Message Unit Reset - instructs the IOC to reset the Reply Post and Free FIFO's. All the Message Frames on Reply Free FIFO are discarded. All posted buffers are freed, and event
notification is turned off. IOC doesn't reply to any outstanding request. This will transfer IOC to READY state.
