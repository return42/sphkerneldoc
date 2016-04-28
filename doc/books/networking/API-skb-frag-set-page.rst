.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-frag-set-page:

=================
skb_frag_set_page
=================

*man skb_frag_set_page(9)*

*4.6.0-rc5*

sets the page contained in a paged fragment of an skb


Synopsis
========

.. c:function:: void skb_frag_set_page( struct sk_buff * skb, int f, struct page * page )

Arguments
=========

``skb``
    the buffer

``f``
    the fragment offset

``page``
    the page to set


Description
===========

Sets the ``f``'th fragment of ``skb`` to contain ``page``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
