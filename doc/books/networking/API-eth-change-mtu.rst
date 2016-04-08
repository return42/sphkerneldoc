
.. _API-eth-change-mtu:

==============
eth_change_mtu
==============

*man eth_change_mtu(9)*

*4.6.0-rc1*

set new MTU size


Synopsis
========

.. c:function:: int eth_change_mtu( struct net_device * dev, int new_mtu )

Arguments
=========

``dev``
    network device

``new_mtu``
    new Maximum Transfer Unit


Description
===========

Allow changing MTU size. Needs to be overridden for devices supporting jumbo frames.
