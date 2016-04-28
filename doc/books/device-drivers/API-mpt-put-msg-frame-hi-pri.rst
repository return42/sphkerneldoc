.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-put-msg-frame-hi-pri:

========================
mpt_put_msg_frame_hi_pri
========================

*man mpt_put_msg_frame_hi_pri(9)*

*4.6.0-rc5*

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

Send a protocol-specific MPT request frame to an IOC using hi-priority
request queue.

This routine posts an MPT request frame to the request post FIFO of a
specific MPT adapter.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
