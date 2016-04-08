
.. _API-sk-eat-skb:

==========
sk_eat_skb
==========

*man sk_eat_skb(9)*

*4.6.0-rc1*

Release a skb if it is no longer needed


Synopsis
========

.. c:function:: void sk_eat_skb( struct sock * sk, struct sk_buff * skb )

Arguments
=========

``sk``
    socket to eat this skb from

``skb``
    socket buffer to eat


Description
===========

This routine must be called with interrupts disabled or with the socket locked so that the sk_buff queue operation is ok.
