
.. _API-skb-propagate-pfmemalloc:

========================
skb_propagate_pfmemalloc
========================

*man skb_propagate_pfmemalloc(9)*

*4.6.0-rc1*

Propagate pfmemalloc if skb is allocated after RX page


Synopsis
========

.. c:function:: void skb_propagate_pfmemalloc( struct page * page, struct sk_buff * skb )

Arguments
=========

``page``
    The page that was allocated from skb_alloc_page

``skb``
    The skb that may need pfmemalloc set
