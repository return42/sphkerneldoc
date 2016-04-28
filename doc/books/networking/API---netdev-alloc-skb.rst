.. -*- coding: utf-8; mode: rst -*-

.. _API---netdev-alloc-skb:

==================
__netdev_alloc_skb
==================

*man __netdev_alloc_skb(9)*

*4.6.0-rc5*

allocate an skbuff for rx on a specific device


Synopsis
========

.. c:function:: struct sk_buff * __netdev_alloc_skb( struct net_device * dev, unsigned int len, gfp_t gfp_mask )

Arguments
=========

``dev``
    network device to receive on

``len``
    length to allocate

``gfp_mask``
    get_free_pages mask, passed to alloc_skb


Description
===========

Allocate a new ``sk_buff`` and assign it a usage count of one. The
buffer has NET_SKB_PAD headroom built in. Users should allocate the
headroom they think they need without accounting for the built in space.
The built in space is used for optimisations.

``NULL`` is returned if there is no free memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
