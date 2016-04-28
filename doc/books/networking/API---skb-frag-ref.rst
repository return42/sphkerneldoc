.. -*- coding: utf-8; mode: rst -*-

.. _API---skb-frag-ref:

==============
__skb_frag_ref
==============

*man __skb_frag_ref(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
