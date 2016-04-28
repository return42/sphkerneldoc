.. -*- coding: utf-8; mode: rst -*-

.. _API---skb-frag-set-page:

===================
__skb_frag_set_page
===================

*man __skb_frag_set_page(9)*

*4.6.0-rc5*

sets the page contained in a paged fragment


Synopsis
========

.. c:function:: void __skb_frag_set_page( skb_frag_t * frag, struct page * page )

Arguments
=========

``frag``
    the paged fragment

``page``
    the page to set


Description
===========

Sets the fragment ``frag`` to contain ``page``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
