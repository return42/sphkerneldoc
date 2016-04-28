.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy-ubufs:

==============
skb_copy_ubufs
==============

*man skb_copy_ubufs(9)*

*4.6.0-rc5*

copy userspace skb frags buffers to kernel


Synopsis
========

.. c:function:: int skb_copy_ubufs( struct sk_buff * skb, gfp_t gfp_mask )

Arguments
=========

``skb``
    the skb to modify

``gfp_mask``
    allocation priority


Description
===========

This must be called on SKBTX_DEV_ZEROCOPY skb. It will copy all frags
into kernel and drop the reference to userspace pages.

If this function is called from an interrupt ``gfp_mask`` must be
``GFP_ATOMIC``.

Returns 0 on success or a negative error code on failure to allocate
kernel memory to copy to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
