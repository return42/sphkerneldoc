
.. _API-netdev-master-upper-dev-link:

============================
netdev_master_upper_dev_link
============================

*man netdev_master_upper_dev_link(9)*

*4.6.0-rc1*

Add a master link to the upper device


Synopsis
========

.. c:function:: int netdev_master_upper_dev_link( struct net_device * dev, struct net_device * upper_dev, void * upper_priv, void * upper_info )

Arguments
=========

``dev``
    device

``upper_dev``
    new upper device

``upper_priv``
    upper device private

``upper_info``
    upper info to be passed down via notifier


Description
===========

Adds a link to device which is upper to this one. In this case, only one master upper device can be linked, although other non-master devices might be linked as well. The caller
must hold the RTNL lock. On a failure a negative errno code is returned. On success the reference counts are adjusted and the function returns zero.
