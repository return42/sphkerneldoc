
.. _API-dev-set-mac-address:

===================
dev_set_mac_address
===================

*man dev_set_mac_address(9)*

*4.6.0-rc1*

Change Media Access Control Address


Synopsis
========

.. c:function:: int dev_set_mac_address( struct net_device * dev, struct sockaddr * sa )

Arguments
=========

``dev``
    device

``sa``
    new address


Description
===========

Change the hardware (MAC) address of the device
