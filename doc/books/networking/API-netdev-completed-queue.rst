.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-completed-queue:

======================
netdev_completed_queue
======================

*man netdev_completed_queue(9)*

*4.6.0-rc5*

report bytes and packets completed by device


Synopsis
========

.. c:function:: void netdev_completed_queue( struct net_device * dev, unsigned int pkts, unsigned int bytes )

Arguments
=========

``dev``
    network device

``pkts``
    actual number of packets sent over the medium

``bytes``
    actual number of bytes sent over the medium


Description
===========

Report the number of bytes and packets transmitted by the network device
hardware queue over the physical medium, ``bytes`` must exactly match
the ``bytes`` amount passed to ``netdev_sent_queue``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
