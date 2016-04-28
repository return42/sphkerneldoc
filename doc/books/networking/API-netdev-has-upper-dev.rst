.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-has-upper-dev:

====================
netdev_has_upper_dev
====================

*man netdev_has_upper_dev(9)*

*4.6.0-rc5*

Check if device is linked to an upper device


Synopsis
========

.. c:function:: bool netdev_has_upper_dev( struct net_device * dev, struct net_device * upper_dev )

Arguments
=========

``dev``
    device

``upper_dev``
    upper device to check


Description
===========

Find out if a device is linked to specified upper device and return true
in case it is. Note that this checks only immediate upper device, not
through a complete stack of devices. The caller must hold the RTNL lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
