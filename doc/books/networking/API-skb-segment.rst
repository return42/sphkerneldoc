
.. _API-skb-segment:

===========
skb_segment
===========

*man skb_segment(9)*

*4.6.0-rc1*

Perform protocol segmentation on skb.


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_segment( struct sk_buff * head_skb, netdev_features_t features )

Arguments
=========

``head_skb``
    buffer to segment

``features``
    features for the output path (see dev->features)


Description
===========

This function performs segmentation on the given skb. It returns a pointer to the first in a list of new skbs for the segments. In case of error it returns ERR_PTR(err).
