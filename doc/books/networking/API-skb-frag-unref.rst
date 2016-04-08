
.. _API-skb-frag-unref:

==============
skb_frag_unref
==============

*man skb_frag_unref(9)*

*4.6.0-rc1*

release a reference on a paged fragment of an skb.


Synopsis
========

.. c:function:: void skb_frag_unref( struct sk_buff * skb, int f )

Arguments
=========

``skb``
    the buffer

``f``
    the fragment offset


Description
===========

Releases a reference on the ``f``'th paged fragment of ``skb``.
