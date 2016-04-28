.. -*- coding: utf-8; mode: rst -*-

.. _API-is-etherdev-addr:

================
is_etherdev_addr
================

*man is_etherdev_addr(9)*

*4.6.0-rc5*

Tell if given Ethernet address belongs to the device.


Synopsis
========

.. c:function:: bool is_etherdev_addr( const struct net_device * dev, const u8 addr[6 + 2] )

Arguments
=========

``dev``
    Pointer to a device structure

``addr[6 + 2]``
    Pointer to a six-byte array containing the Ethernet address


Description
===========

Compare passed address with all addresses of the device. Return true if
the address if one of the device addresses.

Note that this function calls ``ether_addr_equal_64bits`` so take care
of the right padding.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
