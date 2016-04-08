
.. _API-netdev-rx-handler-unregister:

============================
netdev_rx_handler_unregister
============================

*man netdev_rx_handler_unregister(9)*

*4.6.0-rc1*

unregister receive handler


Synopsis
========

.. c:function:: void netdev_rx_handler_unregister( struct net_device * dev )

Arguments
=========

``dev``
    device to unregister a handler from


Description
===========

Unregister a receive handler from a device.

The caller must hold the rtnl_mutex.
