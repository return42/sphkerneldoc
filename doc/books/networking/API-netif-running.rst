
.. _API-netif-running:

=============
netif_running
=============

*man netif_running(9)*

*4.6.0-rc1*

test if up


Synopsis
========

.. c:function:: bool netif_running( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Test if the device has been brought up.
