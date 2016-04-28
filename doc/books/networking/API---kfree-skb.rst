.. -*- coding: utf-8; mode: rst -*-

.. _API---kfree-skb:

===========
__kfree_skb
===========

*man __kfree_skb(9)*

*4.6.0-rc5*

private function


Synopsis
========

.. c:function:: void __kfree_skb( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer


Description
===========

Free an sk_buff. Release anything attached to the buffer. Clean the
state. This is an internal helper function. Users should always call
kfree_skb


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
