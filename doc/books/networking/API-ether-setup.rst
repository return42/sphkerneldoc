
.. _API-ether-setup:

===========
ether_setup
===========

*man ether_setup(9)*

*4.6.0-rc1*

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
