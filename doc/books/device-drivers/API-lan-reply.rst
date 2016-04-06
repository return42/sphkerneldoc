
.. _API-lan-reply:

=========
lan_reply
=========

*man lan_reply(9)*

*4.6.0-rc1*

Handle all data sent from the hardware.


Synopsis
========

.. c:function:: int lan_reply( MPT_ADAPTER * ioc, MPT_FRAME_HDR * mf, MPT_FRAME_HDR * reply )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``mf``
    Pointer to original MPT request frame (NULL if TurboReply)

``reply``
    Pointer to MPT reply frame


Description
===========

Returns 1 indicating original alloc'd request frame ptr should be freed, or 0 if it shouldn't.
