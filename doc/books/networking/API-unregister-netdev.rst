
.. _API-unregister-netdev:

=================
unregister_netdev
=================

*man unregister_netdev(9)*

*4.6.0-rc1*

remove device from the kernel


Synopsis
========

.. c:function:: void unregister_netdev( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

This function shuts down a device interface and removes it from the kernel tables.

This is just a wrapper for unregister_netdevice that takes the rtnl semaphore. In general you want to use this and not unregister_netdevice.
