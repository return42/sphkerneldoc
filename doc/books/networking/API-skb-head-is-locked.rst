.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-head-is-locked:

==================
skb_head_is_locked
==================

*man skb_head_is_locked(9)*

*4.6.0-rc5*

Determine if the skb->head is locked down


Synopsis
========

.. c:function:: bool skb_head_is_locked( const struct sk_buff * skb )

Arguments
=========

``skb``
    skb to check


Description
===========

The head on skbs build around a head frag can be removed if they are not
cloned. This function returns true if the skb head is locked down due to
either being allocated via kmalloc, or by being a clone with multiple
references to the head.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
