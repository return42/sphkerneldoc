.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-set-real-num-rx-queues:

============================
netif_set_real_num_rx_queues
============================

*man netif_set_real_num_rx_queues(9)*

*4.6.0-rc5*

set actual number of RX queues used


Synopsis
========

.. c:function:: int netif_set_real_num_rx_queues( struct net_device * dev, unsigned int rxq )

Arguments
=========

``dev``
    Network device

``rxq``
    Actual number of RX queues


Description
===========

This must be called either with the rtnl_lock held or before
registration of the net device. Returns 0 on success, or a negative
error code. If called before registration, it always succeeds.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
