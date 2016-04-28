.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-frag-ref:

============
skb_frag_ref
============

*man skb_frag_ref(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
