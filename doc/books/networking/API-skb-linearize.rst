.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-linearize:

=============
skb_linearize
=============

*man skb_linearize(9)*

*4.6.0-rc5*

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

If there is no free memory -ENOMEM is returned, otherwise zero is
returned and the old skb data released.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
