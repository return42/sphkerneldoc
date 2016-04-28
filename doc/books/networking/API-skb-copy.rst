.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy:

========
skb_copy
========

*man skb_copy(9)*

*4.6.0-rc5*

create private copy of an sk_buff


Synopsis
========

.. c:function:: struct sk_buff * skb_copy( const struct sk_buff * skb, gfp_t gfp_mask )

Arguments
=========

``skb``
    buffer to copy

``gfp_mask``
    allocation priority


Description
===========

Make a copy of both an ``sk_buff`` and its data. This is used when the
caller wishes to modify the data and needs a private copy of the data to
alter. Returns ``NULL`` on failure or the pointer to the buffer on
success. The returned buffer has a reference count of 1.

As by-product this function converts non-linear ``sk_buff`` to linear
one, so that ``sk_buff`` becomes completely private and caller is
allowed to modify all the data of returned buffer. This means that this
function is not recommended for use in circumstances when only header is
going to be modified. Use ``pskb_copy`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
