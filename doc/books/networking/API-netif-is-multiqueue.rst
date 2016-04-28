.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-is-multiqueue:

===================
netif_is_multiqueue
===================

*man netif_is_multiqueue(9)*

*4.6.0-rc5*

test if device has multiple transmit queues


Synopsis
========

.. c:function:: bool netif_is_multiqueue( const struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Check if device has multiple transmit queues


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
