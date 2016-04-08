
.. _API-netdev-features-change:

======================
netdev_features_change
======================

*man netdev_features_change(9)*

*4.6.0-rc1*

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
