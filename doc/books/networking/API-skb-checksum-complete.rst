.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-checksum-complete:

=====================
skb_checksum_complete
=====================

*man skb_checksum_complete(9)*

*4.6.0-rc5*

Calculate checksum of an entire packet


Synopsis
========

.. c:function:: __sum16 skb_checksum_complete( struct sk_buff * skb )

Arguments
=========

``skb``
    packet to process


Description
===========

This function calculates the checksum over the entire packet plus the
value of skb->csum. The latter can be used to supply the checksum of a
pseudo header as used by TCP/UDP. It returns the checksum.

For protocols that contain complete checksums such as ICMP/TCP/UDP, this
function can be used to verify that checksum on received packets. In
that case the function should return zero if the checksum is correct. In
particular, this function will return zero if skb->ip_summed is
CHECKSUM_UNNECESSARY which indicates that the hardware has already
verified the correctness of the checksum.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
