.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-nl-rcv-msg:

===============
scsi_nl_rcv_msg
===============

*man scsi_nl_rcv_msg(9)*

*4.6.0-rc5*

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

Extracts message from a receive buffer. Validates message header and
calls appropriate transport message handler


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
