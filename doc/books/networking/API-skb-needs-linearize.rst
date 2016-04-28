.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-needs-linearize:

===================
skb_needs_linearize
===================

*man skb_needs_linearize(9)*

*4.6.0-rc5*

check if we need to linearize a given skb depending on the given device
features.


Synopsis
========

.. c:function:: bool skb_needs_linearize( struct sk_buff * skb, netdev_features_t features )

Arguments
=========

``skb``
    socket buffer to check

``features``
    net device features


Returns true if either
======================

1. skb has frag_list and the device doesn't support FRAGLIST, or 2. skb
is fragmented and the device does not support SG.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
