.. -*- coding: utf-8; mode: rst -*-

.. _API-register-netdev:

===============
register_netdev
===============

*man register_netdev(9)*

*4.6.0-rc5*

register a network device


Synopsis
========

.. c:function:: int register_netdev( struct net_device * dev )

Arguments
=========

``dev``
    device to register


Description
===========

Take a completed network device structure and add it to the kernel
interfaces. A ``NETDEV_REGISTER`` message is sent to the netdev notifier
chain. 0 is returned on success. A negative errno code is returned on a
failure to set up the device, or if the name is a duplicate.

This is a wrapper around register_netdevice that takes the rtnl
semaphore and expands the device name if you passed a format string to
alloc_netdev.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
