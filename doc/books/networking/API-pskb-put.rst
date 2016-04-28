.. -*- coding: utf-8; mode: rst -*-

.. _API-pskb-put:

========
pskb_put
========

*man pskb_put(9)*

*4.6.0-rc5*

add data to the tail of a potentially fragmented buffer


Synopsis
========

.. c:function:: unsigned char * pskb_put( struct sk_buff * skb, struct sk_buff * tail, int len )

Arguments
=========

``skb``
    start of the buffer to use

``tail``
    tail fragment of the buffer to use

``len``
    amount of data to add


Description
===========

This function extends the used data area of the potentially fragmented
buffer. ``tail`` must be the last fragment of ``skb`` -- or ``skb``
itself. If this would exceed the total buffer size the kernel will
panic. A pointer to the first byte of the extra data is returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
