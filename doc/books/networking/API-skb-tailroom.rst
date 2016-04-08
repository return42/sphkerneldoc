
.. _API-skb-tailroom:

============
skb_tailroom
============

*man skb_tailroom(9)*

*4.6.0-rc1*

bytes at buffer end


Synopsis
========

.. c:function:: int skb_tailroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the tail of an sk_buff
