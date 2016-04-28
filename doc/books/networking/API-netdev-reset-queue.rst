.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-reset-queue:

==================
netdev_reset_queue
==================

*man netdev_reset_queue(9)*

*4.6.0-rc5*

reset the packets and bytes count of a network device


Synopsis
========

.. c:function:: void netdev_reset_queue( struct net_device * dev_queue )

Arguments
=========

``dev_queue``
    network device


Description
===========

Reset the bytes and packet count of a network device and clear the
software flow control OFF bit for this network device


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
