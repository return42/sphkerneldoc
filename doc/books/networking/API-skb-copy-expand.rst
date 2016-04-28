.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy-expand:

===============
skb_copy_expand
===============

*man skb_copy_expand(9)*

*4.6.0-rc5*

copy and expand sk_buff


Synopsis
========

.. c:function:: struct sk_buff * skb_copy_expand( const struct sk_buff * skb, int newheadroom, int newtailroom, gfp_t gfp_mask )

Arguments
=========

``skb``
    buffer to copy

``newheadroom``
    new free bytes at head

``newtailroom``
    new free bytes at tail

``gfp_mask``
    allocation priority


Description
===========

Make a copy of both an ``sk_buff`` and its data and while doing so
allocate additional space.

This is used when the caller wishes to modify the data and needs a
private copy of the data to alter as well as more space for new fields.
Returns ``NULL`` on failure or the pointer to the buffer on success. The
returned buffer has a reference count of 1.

You must pass ``GFP_ATOMIC`` as the allocation priority if this function
is called from an interrupt.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
