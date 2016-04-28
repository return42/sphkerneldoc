.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-push:

========
skb_push
========

*man skb_push(9)*

*4.6.0-rc5*

add data to the start of a buffer


Synopsis
========

.. c:function:: unsigned char * skb_push( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to use

``len``
    amount of data to add


Description
===========

This function extends the used data area of the buffer at the buffer
start. If this would exceed the total buffer headroom the kernel will
panic. A pointer to the first byte of the extra data is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
