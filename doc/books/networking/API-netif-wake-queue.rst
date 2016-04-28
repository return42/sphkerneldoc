.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-wake-queue:

================
netif_wake_queue
================

*man netif_wake_queue(9)*

*4.6.0-rc5*

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

Allow upper layers to call the device hard_start_xmit routine. Used
for flow control when transmit resources are available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
