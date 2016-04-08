
.. _API---skb-frag-ref:

==============
__skb_frag_ref
==============

*man __skb_frag_ref(9)*

*4.6.0-rc1*

take an addition reference on a paged fragment.


Synopsis
========

.. c:function:: void __skb_frag_ref( skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment


Description
===========

Takes an additional reference on the paged fragment ``frag``.
