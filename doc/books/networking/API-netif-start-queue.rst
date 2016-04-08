
.. _API-netif-start-queue:

=================
netif_start_queue
=================

*man netif_start_queue(9)*

*4.6.0-rc1*

allow transmit


Synopsis
========

.. c:function:: void netif_start_queue( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Allow upper layers to call the device hard_start_xmit routine.
