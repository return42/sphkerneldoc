
.. _API-netif-device-detach:

===================
netif_device_detach
===================

*man netif_device_detach(9)*

*4.6.0-rc1*

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
