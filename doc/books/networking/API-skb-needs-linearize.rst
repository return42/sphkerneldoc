
.. _API-skb-needs-linearize:

===================
skb_needs_linearize
===================

*man skb_needs_linearize(9)*

*4.6.0-rc1*

check if we need to linearize a given skb depending on the given device features.


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

1. skb has frag_list and the device doesn't support FRAGLIST, or 2. skb is fragmented and the device does not support SG.
