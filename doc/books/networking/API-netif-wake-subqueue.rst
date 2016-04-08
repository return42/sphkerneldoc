
.. _API-netif-wake-subqueue:

===================
netif_wake_subqueue
===================

*man netif_wake_subqueue(9)*

*4.6.0-rc1*

allow sending packets on subqueue


Synopsis
========

.. c:function:: void netif_wake_subqueue( struct net_device * dev, u16 queue_index )

Arguments
=========

``dev``
    network device

``queue_index``
    sub queue index


Description
===========

Resume individual transmit queue of a device with multiple transmit queues.
