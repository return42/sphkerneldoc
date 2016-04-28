.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-queue-stopped:

===================
netif_queue_stopped
===================

*man netif_queue_stopped(9)*

*4.6.0-rc5*

test if transmit queue is flowblocked


Synopsis
========

.. c:function:: bool netif_queue_stopped( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Test if transmit queue on device is currently unable to send.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
