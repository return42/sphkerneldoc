
.. _API-netif-device-present:

====================
netif_device_present
====================

*man netif_device_present(9)*

*4.6.0-rc1*

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
