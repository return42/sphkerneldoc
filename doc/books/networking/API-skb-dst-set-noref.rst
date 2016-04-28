.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-dst-set-noref:

=================
skb_dst_set_noref
=================

*man skb_dst_set_noref(9)*

*4.6.0-rc5*

sets skb dst, hopefully, without taking reference


Synopsis
========

.. c:function:: void skb_dst_set_noref( struct sk_buff * skb, struct dst_entry * dst )

Arguments
=========

``skb``
    buffer

``dst``
    dst entry


Description
===========

Sets skb dst, assuming a reference was not taken on dst. If dst entry is
cached, we do not take reference and dst_release will be avoided by
refdst_drop. If dst entry is not cached, we take reference, so that
last dst_release can destroy the dst immediately.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
