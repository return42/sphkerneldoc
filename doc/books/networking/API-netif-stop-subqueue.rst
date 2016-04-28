.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-stop-subqueue:

===================
netif_stop_subqueue
===================

*man netif_stop_subqueue(9)*

*4.6.0-rc5*

stop sending packets on subqueue


Synopsis
========

.. c:function:: void netif_stop_subqueue( struct net_device * dev, u16 queue_index )

Arguments
=========

``dev``
    network device

``queue_index``
    sub queue index


Description
===========

Stop individual transmit queue of a device with multiple transmit
queues.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
