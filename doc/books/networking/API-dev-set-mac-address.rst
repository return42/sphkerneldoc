.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-set-mac-address:

===================
dev_set_mac_address
===================

*man dev_set_mac_address(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
