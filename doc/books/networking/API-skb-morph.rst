
.. _API-skb-morph:

=========
skb_morph
=========

*man skb_morph(9)*

*4.6.0-rc1*

morph one skb into another


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_morph( struct sk_buff * dst, struct sk_buff * src )

Arguments
=========

``dst``
    the skb to receive the contents

``src``
    the skb to supply the contents


Description
===========

This is identical to skb_clone except that the target skb is supplied by the user.

The target skb is returned upon exit.
