
.. _API-mpt-get-msg-frame:

=================
mpt_get_msg_frame
=================

*man mpt_get_msg_frame(9)*

*4.6.0-rc1*

Obtain an MPT request frame from the pool


Synopsis
========

.. c:function:: MPT_FRAME_HDR⋆ mpt_get_msg_frame( u8 cb_idx, MPT_ADAPTER * ioc )

Arguments
=========

``cb_idx``
    Handle of registered MPT protocol driver

``ioc``
    Pointer to MPT adapter structure


Description
===========

Obtain an MPT request frame from the pool (of 1024) that are allocated per MPT adapter.

Returns pointer to a MPT request frame or ``NULL`` if none are available or IOC is not active.
