
.. _API-netif-is-multiqueue:

===================
netif_is_multiqueue
===================

*man netif_is_multiqueue(9)*

*4.6.0-rc1*

test if device has multiple transmit queues


Synopsis
========

.. c:function:: bool netif_is_multiqueue( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Check if device has multiple transmit queues
