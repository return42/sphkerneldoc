
.. _API-netif-oper-up:

=============
netif_oper_up
=============

*man netif_oper_up(9)*

*4.6.0-rc1*

test if device is operational


Synopsis
========

.. c:function:: bool netif_oper_up( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Check if carrier is operational
