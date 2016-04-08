
.. _API---kfree-skb:

===========
__kfree_skb
===========

*man __kfree_skb(9)*

*4.6.0-rc1*

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

Free an sk_buff. Release anything attached to the buffer. Clean the state. This is an internal helper function. Users should always call kfree_skb
