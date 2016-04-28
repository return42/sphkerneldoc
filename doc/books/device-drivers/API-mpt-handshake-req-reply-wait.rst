.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-handshake-req-reply-wait:

============================
mpt_handshake_req_reply_wait
============================

*man mpt_handshake_req_reply_wait(9)*

*4.6.0-rc5*

Send MPT request to and receive reply from IOC via doorbell handshake
method.


Synopsis
========

.. c:function:: int mpt_handshake_req_reply_wait( MPT_ADAPTER * ioc, int reqBytes, u32 * req, int replyBytes, u16 * u16reply, int maxwait, int sleepFlag )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``reqBytes``
    Size of the request in bytes

``req``
    Pointer to MPT request frame

``replyBytes``
    Expected size of the reply in bytes

``u16reply``
    Pointer to area where reply should be written

``maxwait``
    Max wait time for a reply (in seconds)

``sleepFlag``
    Specifies whether the process can sleep


NOTES
=====

It is the callers responsibility to byte-swap fields in the request
which are greater than 1 byte in size. It is also the callers
responsibility to byte-swap response fields which are greater than 1
byte in size.

Returns 0 for success, non-zero for failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
