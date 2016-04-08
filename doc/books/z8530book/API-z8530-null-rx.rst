
.. _API-z8530-null-rx:

=============
z8530_null_rx
=============

*man z8530_null_rx(9)*

*4.6.0-rc1*

Discard a packet


Synopsis
========

.. c:function:: void z8530_null_rx( struct z8530_channel * c, struct sk_buff * skb )

Arguments
=========

``c``
    The channel the packet arrived on

``skb``
    The buffer


Description
===========

We point the receive handler at this function when idle. Instead of processing the frames we get to throw them away.
