
.. _API-netdev-upper-dev-unlink:

=======================
netdev_upper_dev_unlink
=======================

*man netdev_upper_dev_unlink(9)*

*4.6.0-rc1*

Removes a link to upper device


Synopsis
========

.. c:function:: void netdev_upper_dev_unlink( struct net_device * dev, struct net_device * upper_dev )

Arguments
=========

``dev``
    device

``upper_dev``
    new upper device


Description
===========

Removes a link to device which is upper to this one. The caller must hold the RTNL lock.
