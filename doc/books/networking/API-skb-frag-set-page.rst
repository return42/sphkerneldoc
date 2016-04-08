
.. _API-skb-frag-set-page:

=================
skb_frag_set_page
=================

*man skb_frag_set_page(9)*

*4.6.0-rc1*

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
