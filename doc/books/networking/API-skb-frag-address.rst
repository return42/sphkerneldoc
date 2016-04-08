
.. _API-skb-frag-address:

================
skb_frag_address
================

*man skb_frag_address(9)*

*4.6.0-rc1*

gets the address of the data contained in a paged fragment


Synopsis
========

.. c:function:: void ⋆ skb_frag_address( const skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment buffer


Description
===========

Returns the address of the data within ``frag``. The page must already be mapped.
