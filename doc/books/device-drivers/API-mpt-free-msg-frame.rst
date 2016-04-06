
.. _API-mpt-free-msg-frame:

==================
mpt_free_msg_frame
==================

*man mpt_free_msg_frame(9)*

*4.6.0-rc1*

Place MPT request frame back on FreeQ.


Synopsis
========

.. c:function:: void mpt_free_msg_frame( MPT_ADAPTER * ioc, MPT_FRAME_HDR * mf )

Arguments
=========

``ioc``
    Pointer to MPT adapter structure

``mf``
    Pointer to MPT request frame


Description
===========

This routine places a MPT request frame back on the MPT adapter's FreeQ.
