.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-cap-txqueue:

==================
netdev_cap_txqueue
==================

*man netdev_cap_txqueue(9)*

*4.6.0-rc5*

check if selected tx queue exceeds device queues


Synopsis
========

.. c:function:: u16 netdev_cap_txqueue( struct net_device * dev, u16 queue_index )

Arguments
=========

``dev``
    network device

``queue_index``
    given tx queue index


Description
===========

Returns 0 if given tx queue index >= number of device tx queues,
otherwise returns the originally passed tx queue index.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
