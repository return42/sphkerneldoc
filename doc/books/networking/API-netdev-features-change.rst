.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-features-change:

======================
netdev_features_change
======================

*man netdev_features_change(9)*

*4.6.0-rc5*

device changes features


Synopsis
========

.. c:function:: void netdev_features_change( struct net_device * dev )

Arguments
=========

``dev``
    device to cause notification


Description
===========

Called to indicate a device has changed features.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
