.. -*- coding: utf-8; mode: rst -*-

.. _API-WaitForDoorbellAck:

==================
WaitForDoorbellAck
==================

*man WaitForDoorbellAck(9)*

*4.6.0-rc5*

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

This routine waits (up to ~2 seconds max) for IOC doorbell handshake
ACKnowledge, indicated by the IOP_DOORBELL_STATUS bit in its IntStatus
register being clear.

Returns a negative value on failure, else wait loop count.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
