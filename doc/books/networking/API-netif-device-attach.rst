
.. _API-netif-device-attach:

===================
netif_device_attach
===================

*man netif_device_attach(9)*

*4.6.0-rc1*

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
