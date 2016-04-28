.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-device-present:

====================
netif_device_present
====================

*man netif_device_present(9)*

*4.6.0-rc5*

is device available or removed


Synopsis
========

.. c:function:: bool netif_device_present( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Check if device has not been removed from system.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
