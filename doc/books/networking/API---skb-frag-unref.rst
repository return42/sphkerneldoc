
.. _API---skb-frag-unref:

================
__skb_frag_unref
================

*man __skb_frag_unref(9)*

*4.6.0-rc1*

release a reference on a paged fragment.


Synopsis
========

.. c:function:: void __skb_frag_unref( skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment


Description
===========

Releases a reference on the paged fragment ``frag``.
