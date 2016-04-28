.. -*- coding: utf-8; mode: rst -*-

.. _API-consume-skb:

===========
consume_skb
===========

*man consume_skb(9)*

*4.6.0-rc5*

free an skbuff


Synopsis
========

.. c:function:: void consume_skb( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to free


Description
===========

Drop a ref to the buffer and free it if the usage count has hit zero
Functions identically to kfree_skb, but kfree_skb assumes that the
frame is being dropped after a failure and notes that


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
