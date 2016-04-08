
.. _API-netdev-notify-peers:

===================
netdev_notify_peers
===================

*man netdev_notify_peers(9)*

*4.6.0-rc1*

notify network peers about existence of ``dev``


Synopsis
========

.. c:function:: void netdev_notify_peers( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Generate traffic such that interested network peers are aware of ``dev``, such as by generating a gratuitous ARP. This may be used when a device wants to inform the rest of the
network about some sort of reconfiguration such as a failover event or virtual machine migration.
