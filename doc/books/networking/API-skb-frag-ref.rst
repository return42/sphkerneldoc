
.. _API-skb-frag-ref:

============
skb_frag_ref
============

*man skb_frag_ref(9)*

*4.6.0-rc1*

take an addition reference on a paged fragment of an skb.


Synopsis
========

.. c:function:: void skb_frag_ref( struct sk_buff * skb, int f )

Arguments
=========

``skb``
    the buffer

``f``
    the fragment offset.


Description
===========

Takes an additional reference on the ``f``'th paged fragment of ``skb``.
