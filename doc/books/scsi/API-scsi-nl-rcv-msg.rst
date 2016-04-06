
.. _API-scsi-nl-rcv-msg:

===============
scsi_nl_rcv_msg
===============

*man scsi_nl_rcv_msg(9)*

*4.6.0-rc1*

Receive message handler.


Synopsis
========

.. c:function:: void scsi_nl_rcv_msg( struct sk_buff * skb )

Arguments
=========

``skb``
    socket receive buffer


Description
===========

Extracts message from a receive buffer. Validates message header and calls appropriate transport message handler
