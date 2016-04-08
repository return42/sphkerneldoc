
.. _API-kfree-skb:

=========
kfree_skb
=========

*man kfree_skb(9)*

*4.6.0-rc1*

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

Drop a reference to the buffer and free it if the usage count has hit zero.
