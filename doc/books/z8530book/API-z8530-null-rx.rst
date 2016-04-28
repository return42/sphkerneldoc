.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-null-rx:

=============
z8530_null_rx
=============

*man z8530_null_rx(9)*

*4.6.0-rc5*

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

We point the receive handler at this function when idle. Instead of
processing the frames we get to throw them away.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
