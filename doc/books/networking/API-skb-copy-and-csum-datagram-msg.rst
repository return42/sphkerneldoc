
.. _API-skb-copy-and-csum-datagram-msg:

==============================
skb_copy_and_csum_datagram_msg
==============================

*man skb_copy_and_csum_datagram_msg(9)*

*4.6.0-rc1*

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
