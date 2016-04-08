
.. _API---skb-fill-page-desc:

====================
__skb_fill_page_desc
====================

*man __skb_fill_page_desc(9)*

*4.6.0-rc1*

initialise a paged fragment in an skb


Synopsis
========

.. c:function:: void __skb_fill_page_desc( struct sk_buff * skb, int i, struct page * page, int off, int size )

Arguments
=========

``skb``
    buffer containing fragment to be initialised

``i``
    paged fragment index to initialise

``page``
    the page to use for this fragment

``off``
    the offset to the data with ``page``

``size``
    the length of the data


Description
===========

Initialises the ``i``'th fragment of ``skb`` to point to ``size`` bytes at offset ``off`` within ``page``.

Does not take any additional reference on the fragment.
