.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-update-features:

======================
netdev_update_features
======================

*man netdev_update_features(9)*

*4.6.0-rc5*

recalculate device features


Synopsis
========

.. c:function:: void netdev_update_features( struct net_device * dev )

Arguments
=========

``dev``
    the device to check


Description
===========

Recalculate dev->features set and send notifications if it has changed.
Should be called after driver or hardware dependent conditions might
have changed that influence the features.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
