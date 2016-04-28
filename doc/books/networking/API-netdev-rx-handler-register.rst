.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-rx-handler-register:

==========================
netdev_rx_handler_register
==========================

*man netdev_rx_handler_register(9)*

*4.6.0-rc5*

register receive handler


Synopsis
========

.. c:function:: int netdev_rx_handler_register( struct net_device * dev, rx_handler_func_t * rx_handler, void * rx_handler_data )

Arguments
=========

``dev``
    device to register a handler for

``rx_handler``
    receive handler to register

``rx_handler_data``
    data pointer that is used by rx handler


Description
===========

Register a receive handler for a device. This handler will then be
called from __netif_receive_skb. A negative errno code is returned
on a failure.

The caller must hold the rtnl_mutex.

For a general description of rx_handler, see enum rx_handler_result.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
