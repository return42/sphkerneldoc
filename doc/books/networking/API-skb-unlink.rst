
.. _API-skb-unlink:

==========
skb_unlink
==========

*man skb_unlink(9)*

*4.6.0-rc1*

remove a buffer from a list


Synopsis
========

.. c:function:: void skb_unlink( struct sk_buff * skb, struct sk_buff_head * list )

Arguments
=========

``skb``
    buffer to remove

``list``
    list to use


Description
===========

Remove a packet from a list. The list locks are taken and this function is atomic with respect to other list locked calls

You must know what list the SKB is on.
