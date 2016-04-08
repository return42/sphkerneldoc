
.. _API-netif-stop-queue:

================
netif_stop_queue
================

*man netif_stop_queue(9)*

*4.6.0-rc1*

stop transmitted packets


Synopsis
========

.. c:function:: void netif_stop_queue( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Stop upper layers calling the device hard_start_xmit routine. Used for flow control when transmit resources are unavailable.
