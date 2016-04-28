.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-master-upper-dev-get:

===========================
netdev_master_upper_dev_get
===========================

*man netdev_master_upper_dev_get(9)*

*4.6.0-rc5*

Get master upper device


Synopsis
========

.. c:function:: struct net_device * netdev_master_upper_dev_get( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Find a master upper device and return pointer to it or NULL in case it's
not there. The caller must hold the RTNL lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
