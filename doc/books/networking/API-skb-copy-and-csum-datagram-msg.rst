.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy-and-csum-datagram-msg:

==============================
skb_copy_and_csum_datagram_msg
==============================

*man skb_copy_and_csum_datagram_msg(9)*

*4.6.0-rc5*

Copy and checksum skb to user iovec.


Synopsis
========

.. c:function:: int skb_copy_and_csum_datagram_msg( struct sk_buff * skb, int hlen, struct msghdr * msg )

Arguments
=========

``skb``
    skbuff

``hlen``
    hardware length

``msg``
    destination


Description
===========

Caller _must_ check that skb will fit to this iovec.


Returns
=======

0 - success. -EINVAL - checksum failure. -EFAULT - fault during copy.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
