
.. _API-unregister-netdevice-queue:

==========================
unregister_netdevice_queue
==========================

*man unregister_netdevice_queue(9)*

*4.6.0-rc1*

remove device from the kernel


Synopsis
========

.. c:function:: void unregister_netdevice_queue( struct net_device * dev, struct list_head * head )

Arguments
=========

``dev``
    device

``head``
    list


Description
===========

This function shuts down a device interface and removes it from the kernel tables. If head not NULL, device is queued to be unregistered later.

Callers must hold the rtnl semaphore. You may want ``unregister_netdev`` instead of this.
