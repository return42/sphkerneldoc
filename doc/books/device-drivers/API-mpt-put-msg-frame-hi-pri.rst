
.. _API-mpt-put-msg-frame-hi-pri:

========================
mpt_put_msg_frame_hi_pri
========================

*man mpt_put_msg_frame_hi_pri(9)*

*4.6.0-rc1*

Send a hi-pri protocol-specific MPT request frame


Synopsis
========

.. c:function:: void mpt_put_msg_frame_hi_pri( u8 cb_idx, MPT_ADAPTER * ioc, MPT_FRAME_HDR * mf )

Arguments
=========

``cb_idx``
    Handle of registered MPT protocol driver

``ioc``
    Pointer to MPT adapter structure

``mf``
    Pointer to MPT request frame


Description
===========

Send a protocol-specific MPT request frame to an IOC using hi-priority request queue.

This routine posts an MPT request frame to the request post FIFO of a specific MPT adapter.
