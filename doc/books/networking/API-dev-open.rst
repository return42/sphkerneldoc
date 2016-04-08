
.. _API-dev-open:

========
dev_open
========

*man dev_open(9)*

*4.6.0-rc1*

prepare an interface for use.


Synopsis
========

.. c:function:: int dev_open( struct net_device * dev )

Arguments
=========

``dev``
    device to open


Description
===========

Takes a device from down to up state. The device's private open function is invoked and then the multicast lists are loaded. Finally the device is moved into the up state and a
``NETDEV_UP`` message is sent to the netdev notifier chain.

Calling this function on an active interface is a nop. On a failure a negative errno code is returned.
