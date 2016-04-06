
.. _API-WaitForDoorbellReply:

====================
WaitForDoorbellReply
====================

*man WaitForDoorbellReply(9)*

*4.6.0-rc1*

Wait for and capture an IOC handshake reply.


Synopsis
========

.. c:function:: int WaitForDoorbellReply( MPT_ADAPTER * ioc, int howlong, int sleepFlag )

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

This routine polls the IOC for a handshake reply, 16 bits at a time. Reply is cached to IOC private area large enough to hold a maximum of 128 bytes of reply data.

Returns a negative value on failure, else size of reply in WORDS.
