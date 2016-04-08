
.. _API-netdev-master-upper-dev-get:

===========================
netdev_master_upper_dev_get
===========================

*man netdev_master_upper_dev_get(9)*

*4.6.0-rc1*

Get master upper device


Synopsis
========

.. c:function:: struct net_device ⋆ netdev_master_upper_dev_get( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Find a master upper device and return pointer to it or NULL in case it's not there. The caller must hold the RTNL lock.
