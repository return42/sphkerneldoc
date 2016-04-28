.. -*- coding: utf-8; mode: rst -*-

.. _API-kfree-skb:

=========
kfree_skb
=========

*man kfree_skb(9)*

*4.6.0-rc5*

free an sk_buff


Synopsis
========

.. c:function:: void kfree_skb( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to free


Description
===========

Drop a reference to the buffer and free it if the usage count has hit
zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
