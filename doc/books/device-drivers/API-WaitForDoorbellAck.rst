
.. _API-WaitForDoorbellAck:

==================
WaitForDoorbellAck
==================

*man WaitForDoorbellAck(9)*

*4.6.0-rc1*

Wait for IOC doorbell handshake acknowledge


Synopsis
========

.. c:function:: int WaitForDoorbellAck( MPT_ADAPTER * ioc, int howlong, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``howlong``
    How long to wait (in seconds)

``sleepFlag``
    Specifies whether the process can sleep


Description
===========

This routine waits (up to ~2 seconds max) for IOC doorbell handshake ACKnowledge, indicated by the IOP_DOORBELL_STATUS bit in its IntStatus register being clear.

Returns a negative value on failure, else wait loop count.
