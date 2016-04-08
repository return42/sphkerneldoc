
.. _API-netif-wake-queue:

================
netif_wake_queue
================

*man netif_wake_queue(9)*

*4.6.0-rc1*

restart transmit


Synopsis
========

.. c:function:: void netif_wake_queue( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Allow upper layers to call the device hard_start_xmit routine. Used for flow control when transmit resources are available.
