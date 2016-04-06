
.. _API-mptbase-reply:

=============
mptbase_reply
=============

*man mptbase_reply(9)*

*4.6.0-rc1*

MPT base driver's callback routine


Synopsis
========

.. c:function:: int mptbase_reply( MPT_ADAPTER * ioc, MPT_FRAME_HDR * req, MPT_FRAME_HDR * reply )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``req``
    Pointer to original MPT request frame

``reply``
    Pointer to MPT reply frame (NULL if TurboReply)


Description
===========

MPT base driver's callback routine; all base driver “internal” request/reply processing is routed here. Currently used for EventNotification and EventAck handling.

Returns 1 indicating original alloc'd request frame ptr should be freed, or 0 if it shouldn't.
