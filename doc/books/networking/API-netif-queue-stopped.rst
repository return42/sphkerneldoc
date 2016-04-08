
.. _API-netif-queue-stopped:

===================
netif_queue_stopped
===================

*man netif_queue_stopped(9)*

*4.6.0-rc1*

test if transmit queue is flowblocked


Synopsis
========

.. c:function:: bool netif_queue_stopped( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Test if transmit queue on device is currently unable to send.
