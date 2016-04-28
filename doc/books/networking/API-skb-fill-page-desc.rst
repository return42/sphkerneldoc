.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-fill-page-desc:

==================
skb_fill_page_desc
==================

*man skb_fill_page_desc(9)*

*4.6.0-rc5*

initialise a paged fragment in an skb


Synopsis
========

.. c:function:: void skb_fill_page_desc( struct sk_buff * skb, int i, struct page * page, int off, int size )

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

As per ``__skb_fill_page_desc`` -- initialises the ``i``'th fragment of
``skb`` to point to ``size`` bytes at offset ``off`` within ``page``. In
addition updates ``skb`` such that ``i`` is the last fragment.

Does not take any additional reference on the fragment.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
