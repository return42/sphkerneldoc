.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-upper-dev-link:

=====================
netdev_upper_dev_link
=====================

*man netdev_upper_dev_link(9)*

*4.6.0-rc5*

Add a link to the upper device


Synopsis
========

.. c:function:: int netdev_upper_dev_link( struct net_device * dev, struct net_device * upper_dev )

Arguments
=========

``dev``
    device

``upper_dev``
    new upper device


Description
===========

Adds a link to device which is upper to this one. The caller must hold
the RTNL lock. On a failure a negative errno code is returned. On
success the reference counts are adjusted and the function returns zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
