.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-linearize-cow:

=================
skb_linearize_cow
=================

*man skb_linearize_cow(9)*

*4.6.0-rc5*

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

If there is no free memory -ENOMEM is returned, otherwise zero is
returned and the old skb data released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
