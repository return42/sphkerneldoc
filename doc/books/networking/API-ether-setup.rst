.. -*- coding: utf-8; mode: rst -*-

.. _API-ether-setup:

===========
ether_setup
===========

*man ether_setup(9)*

*4.6.0-rc5*

setup Ethernet network device


Synopsis
========

.. c:function:: void ether_setup( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Fill in the fields of the device structure with Ethernet-generic values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
