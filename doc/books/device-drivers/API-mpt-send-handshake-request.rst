.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-send-handshake-request:

==========================
mpt_send_handshake_request
==========================

*man mpt_send_handshake_request(9)*

*4.6.0-rc5*

Send MPT request via doorbell handshake method.


Synopsis
========

.. c:function:: int mpt_send_handshake_request( u8 cb_idx, MPT_ADAPTER * ioc, int reqBytes, u32 * req, int sleepFlag )

Arguments
=========

``cb_idx``
    Handle of registered MPT protocol driver

``ioc``
    Pointer to MPT adapter structure

``reqBytes``
    Size of the request in bytes

``req``
    Pointer to MPT request frame

``sleepFlag``
    Use schedule if CAN_SLEEP else use udelay.


Description
===========

This routine is used exclusively to send MptScsiTaskMgmt requests since
they are required to be sent via doorbell handshake.


NOTE
====

It is the callers responsibility to byte-swap fields in the request
which are greater than 1 byte in size.

Returns 0 for success, non-zero for failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
