.. -*- coding: utf-8; mode: rst -*-

.. _API-register-netdevice:

==================
register_netdevice
==================

*man register_netdevice(9)*

*4.6.0-rc5*

register a network device


Synopsis
========

.. c:function:: int register_netdevice( struct net_device * dev )

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

Callers must hold the rtnl semaphore. You may want ``register_netdev``
instead of this.


BUGS
====

The locking appears insufficient to guarantee two parallel registers
will not get the same name.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
