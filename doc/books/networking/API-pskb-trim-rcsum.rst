
.. _API-pskb-trim-rcsum:

===============
pskb_trim_rcsum
===============

*man pskb_trim_rcsum(9)*

*4.6.0-rc1*

trim received skb and update checksum


Synopsis
========

.. c:function:: int pskb_trim_rcsum( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to trim

``len``
    new length


Description
===========

This is exactly the same as pskb_trim except that it ensures the checksum of received packets are still valid after the operation.
