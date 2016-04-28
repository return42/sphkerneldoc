.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-frag-unref:

==============
skb_frag_unref
==============

*man skb_frag_unref(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
