.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-unshare:

===========
skb_unshare
===========

*man skb_unshare(9)*

*4.6.0-rc5*

make a copy of a shared buffer


Synopsis
========

.. c:function:: struct sk_buff * skb_unshare( struct sk_buff * skb, gfp_t pri )

Arguments
=========

``skb``
    buffer to check

``pri``
    priority for memory allocation


Description
===========

If the socket buffer is a clone then this function creates a new copy of
the data, drops a reference count on the old copy and returns the new
copy with the reference count at 1. If the buffer is not a clone the
original buffer is returned. When called with a spinlock held or from
interrupt state ``pri`` must be ``GFP_ATOMIC``

``NULL`` is returned on a memory allocation failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
