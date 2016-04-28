.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-sent-queue:

=================
netdev_sent_queue
=================

*man netdev_sent_queue(9)*

*4.6.0-rc5*

report the number of bytes queued to hardware


Synopsis
========

.. c:function:: void netdev_sent_queue( struct net_device * dev, unsigned int bytes )

Arguments
=========

``dev``
    network device

``bytes``
    number of bytes queued to the hardware device queue


Description
===========

Report the number of bytes queued for sending/completion to the network
device hardware queue. ``bytes`` should be a good approximation and
should exactly match ``netdev_completed_queue`` ``bytes``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
