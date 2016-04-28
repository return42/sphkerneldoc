.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-frag-page:

=============
skb_frag_page
=============

*man skb_frag_page(9)*

*4.6.0-rc5*

retrieve the page referred to by a paged fragment


Synopsis
========

.. c:function:: struct page * skb_frag_page( const skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment


Description
===========

Returns the ``struct page`` associated with ``frag``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
