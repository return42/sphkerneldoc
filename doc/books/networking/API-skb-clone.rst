
.. _API-skb-clone:

=========
skb_clone
=========

*man skb_clone(9)*

*4.6.0-rc1*

duplicate an sk_buff


Synopsis
========

.. c:function:: struct sk_buff ⋆ skb_clone( struct sk_buff * skb, gfp_t gfp_mask )

Arguments
=========

``skb``
    buffer to clone

``gfp_mask``
    allocation priority


Description
===========

Duplicate an ``sk_buff``. The new one is not owned by a socket. Both copies share the same packet data but not structure. The new buffer has a reference count of 1. If the
allocation fails the function returns ``NULL`` otherwise the new buffer is returned.

If this function is called from an interrupt ``gfp_mask`` must be ``GFP_ATOMIC``.
