.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-device-detach:

===================
netif_device_detach
===================

*man netif_device_detach(9)*

*4.6.0-rc5*

mark device as removed


Synopsis
========

.. c:function:: void netif_device_detach( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Mark device as removed from system and therefore no longer available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
