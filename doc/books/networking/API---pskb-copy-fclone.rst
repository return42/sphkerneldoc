.. -*- coding: utf-8; mode: rst -*-

.. _API---pskb-copy-fclone:

==================
__pskb_copy_fclone
==================

*man __pskb_copy_fclone(9)*

*4.6.0-rc5*

create copy of an sk_buff with private head.


Synopsis
========

.. c:function:: struct sk_buff * __pskb_copy_fclone( struct sk_buff * skb, int headroom, gfp_t gfp_mask, bool fclone )

Arguments
=========

``skb``
    buffer to copy

``headroom``
    headroom of new skb

``gfp_mask``
    allocation priority

``fclone``
    if true allocate the copy of the skb from the fclone cache instead
    of the head cache; it is recommended to set this to true for the
    cases where the copy will likely be cloned


Description
===========

Make a copy of both an ``sk_buff`` and part of its data, located in
header. Fragmented data remain shared. This is used when the caller
wishes to modify only header of ``sk_buff`` and needs private copy of
the header to alter. Returns ``NULL`` on failure or the pointer to the
buffer on success. The returned buffer has a reference count of 1.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
