.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-frag-address:

================
skb_frag_address
================

*man skb_frag_address(9)*

*4.6.0-rc5*

gets the address of the data contained in a paged fragment


Synopsis
========

.. c:function:: void * skb_frag_address( const skb_frag_t * frag )

Arguments
=========

``frag``
    the paged fragment buffer


Description
===========

Returns the address of the data within ``frag``. The page must already
be mapped.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
