
.. _API-skb-linearize-cow:

=================
skb_linearize_cow
=================

*man skb_linearize_cow(9)*

*4.6.0-rc1*

make sure skb is linear and writable


Synopsis
========

.. c:function:: int skb_linearize_cow( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to process


Description
===========

If there is no free memory -ENOMEM is returned, otherwise zero is returned and the old skb data released.
