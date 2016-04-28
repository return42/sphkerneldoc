.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-device-attach:

===================
netif_device_attach
===================

*man netif_device_attach(9)*

*4.6.0-rc5*

mark device as attached


Synopsis
========

.. c:function:: void netif_device_attach( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Mark device as attached from system and restart if needed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
