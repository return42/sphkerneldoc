
.. _API-skb-headroom:

============
skb_headroom
============

*man skb_headroom(9)*

*4.6.0-rc1*

bytes at buffer head


Synopsis
========

.. c:function:: unsigned int skb_headroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the head of an ``sk_buff``.
