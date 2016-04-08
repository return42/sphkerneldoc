
.. _API-netdev-alloc-skb:

================
netdev_alloc_skb
================

*man netdev_alloc_skb(9)*

*4.6.0-rc1*

allocate an skbuff for rx on a specific device


Synopsis
========

.. c:function:: struct sk_buff ⋆ netdev_alloc_skb( struct net_device * dev, unsigned int length )

Arguments
=========

``dev``
    network device to receive on

``length``
    length to allocate


Description
===========

Allocate a new ``sk_buff`` and assign it a usage count of one. The buffer has unspecified headroom built in. Users should allocate the headroom they think they need without
accounting for the built in space. The built in space is used for optimisations.

``NULL`` is returned if there is no free memory. Although this function allocates memory it can be called from an interrupt.
