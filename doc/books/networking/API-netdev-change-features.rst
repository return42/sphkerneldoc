.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-change-features:

======================
netdev_change_features
======================

*man netdev_change_features(9)*

*4.6.0-rc5*

recalculate device features


Synopsis
========

.. c:function:: void netdev_change_features( struct net_device * dev )

Arguments
=========

``dev``
    the device to check


Description
===========

Recalculate dev->features set and send notifications even if they have
not changed. Should be called instead of ``netdev_update_features`` if
also dev->vlan_features might have changed to allow the changes to be
propagated to stacked VLAN devices.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
