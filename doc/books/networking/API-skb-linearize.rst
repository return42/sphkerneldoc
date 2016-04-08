
.. _API-skb-linearize:

=============
skb_linearize
=============

*man skb_linearize(9)*

*4.6.0-rc1*

convert paged skb to linear one


Synopsis
========

.. c:function:: int skb_linearize( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to linarize


Description
===========

If there is no free memory -ENOMEM is returned, otherwise zero is returned and the old skb data released.
