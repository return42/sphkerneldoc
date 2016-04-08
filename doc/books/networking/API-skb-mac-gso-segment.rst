
.. _API-skb-mac-gso-segment:

===================
skb_mac_gso_segment
===================

*man skb_mac_gso_segment(9)*

*4.6.0-rc1*

mac layer segmentation handler.


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_mac_gso_segment( struct sk_buff * skb, netdev_features_t features )

Arguments
=========

``skb``
    buffer to segment

``features``
    features for the output path (see dev->features)
