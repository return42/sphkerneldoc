.. -*- coding: utf-8; mode: rst -*-

.. _API---skb-frag-unref:

================
__skb_frag_unref
================

*man __skb_frag_unref(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
