
.. _API-skb-append:

==========
skb_append
==========

*man skb_append(9)*

*4.6.0-rc1*

append a buffer


Synopsis
========

.. c:function:: void skb_append( struct sk_buff * old, struct sk_buff * newsk, struct sk_buff_head * list )

Arguments
=========

``old``
    buffer to insert after

``newsk``
    buffer to insert

``list``
    list to use


Description
===========

Place a packet after a given packet in a list. The list locks are taken and this function is atomic with respect to other list locked calls. A buffer cannot be placed on two lists
at the same time.
