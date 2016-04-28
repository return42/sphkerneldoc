.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-start-queue:

=================
netif_start_queue
=================

*man netif_start_queue(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
