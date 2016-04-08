
.. _API-skb-insert:

==========
skb_insert
==========

*man skb_insert(9)*

*4.6.0-rc1*

insert a buffer


Synopsis
========

.. c:function:: void skb_insert( struct sk_buff * old, struct sk_buff * newsk, struct sk_buff_head * list )

Arguments
=========

``old``
    buffer to insert before

``newsk``
    buffer to insert

``list``
    list to use


Description
===========

Place a packet before a given packet in a list. The list locks are taken and this function is atomic with respect to other list locked calls.

A buffer cannot be placed on two lists at the same time.
