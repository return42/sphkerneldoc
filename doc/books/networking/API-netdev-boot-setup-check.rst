
.. _API-netdev-boot-setup-check:

=======================
netdev_boot_setup_check
=======================

*man netdev_boot_setup_check(9)*

*4.6.0-rc1*

check boot time settings


Synopsis
========

.. c:function:: int netdev_boot_setup_check( struct net_device * dev )

Arguments
=========

``dev``
    the netdevice


Description
===========

Check boot time settings for the device. The found settings are set for the device to be used later in the device probing. Returns 0 if no settings found, 1 if they are.
