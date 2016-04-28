.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-share-check:

===============
skb_share_check
===============

*man skb_share_check(9)*

*4.6.0-rc5*

check if buffer is shared and if so clone it


Synopsis
========

.. c:function:: struct sk_buff * skb_share_check( struct sk_buff * skb, gfp_t pri )

Arguments
=========

``skb``
    buffer to check

``pri``
    priority for memory allocation


Description
===========

If the buffer is shared the buffer is cloned and the old copy drops a
reference. A new clone with a single reference is returned. If the
buffer is not shared the original buffer is returned. When being called
from interrupt status or with spinlocks held pri must be GFP_ATOMIC.

NULL is returned on a memory allocation failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
