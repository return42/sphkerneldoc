.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-rx-handler-unregister:

============================
netdev_rx_handler_unregister
============================

*man netdev_rx_handler_unregister(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
