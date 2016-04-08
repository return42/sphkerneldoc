
.. _API---skb-gso-segment:

=================
__skb_gso_segment
=================

*man __skb_gso_segment(9)*

*4.6.0-rc1*

Perform segmentation on skb.


Synopsis
========

.. c:function:: struct sk_buff ⋆ __skb_gso_segment( struct sk_buff * skb, netdev_features_t features, bool tx_path )

Arguments
=========

``skb``
    buffer to segment

``features``
    features for the output path (see dev->features)

``tx_path``
    whether it is called in TX path


Description
===========

This function segments the given skb and returns a list of segments.

It may return NULL if the skb requires no segmentation. This is only possible when GSO is used for verifying header integrity.

Segmentation preserves SKB_SGO_CB_OFFSET bytes of previous skb cb.
