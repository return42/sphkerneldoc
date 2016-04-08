
.. _API-skb-checksum-none-assert:

========================
skb_checksum_none_assert
========================

*man skb_checksum_none_assert(9)*

*4.6.0-rc1*

make sure skb ip_summed is CHECKSUM_NONE


Synopsis
========

.. c:function:: void skb_checksum_none_assert( const struct sk_buff * skb )

Arguments
=========

``skb``
    skb to check


Description
===========

fresh skbs have their ip_summed set to CHECKSUM_NONE. Instead of forcing ip_summed to CHECKSUM_NONE, we can use this helper, to document places where we make this assertion.
