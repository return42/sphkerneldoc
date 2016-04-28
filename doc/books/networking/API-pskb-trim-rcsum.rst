.. -*- coding: utf-8; mode: rst -*-

.. _API-pskb-trim-rcsum:

===============
pskb_trim_rcsum
===============

*man pskb_trim_rcsum(9)*

*4.6.0-rc5*

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

This is exactly the same as pskb_trim except that it ensures the
checksum of received packets are still valid after the operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
