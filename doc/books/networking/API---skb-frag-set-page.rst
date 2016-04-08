
.. _API---skb-frag-set-page:

===================
__skb_frag_set_page
===================

*man __skb_frag_set_page(9)*

*4.6.0-rc1*

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
