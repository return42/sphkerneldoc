.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-stop-queue:

================
netif_stop_queue
================

*man netif_stop_queue(9)*

*4.6.0-rc5*

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

Stop upper layers calling the device hard_start_xmit routine. Used for
flow control when transmit resources are unavailable.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
