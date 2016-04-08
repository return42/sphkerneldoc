
.. _API-skb-frag-page:

=============
skb_frag_page
=============

*man skb_frag_page(9)*

*4.6.0-rc1*

retrieve the page referred to by a paged fragment


Synopsis
========

.. c:function:: struct page ⋆ skb_frag_page( const skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment


Description
===========

Returns the ``struct page`` associated with ``frag``.
