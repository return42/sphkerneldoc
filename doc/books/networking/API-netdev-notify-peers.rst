.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-notify-peers:

===================
netdev_notify_peers
===================

*man netdev_notify_peers(9)*

*4.6.0-rc5*

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

Generate traffic such that interested network peers are aware of
``dev``, such as by generating a gratuitous ARP. This may be used when a
device wants to inform the rest of the network about some sort of
reconfiguration such as a failover event or virtual machine migration.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
