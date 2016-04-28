.. -*- coding: utf-8; mode: rst -*-

.. _API---netif-subqueue-stopped:

========================
__netif_subqueue_stopped
========================

*man __netif_subqueue_stopped(9)*

*4.6.0-rc5*

test status of subqueue


Synopsis
========

.. c:function:: bool __netif_subqueue_stopped( const struct net_device * dev, u16 queue_index )

Arguments
=========

``dev``
    network device

``queue_index``
    sub queue index


Description
===========

Check individual transmit queue of a device with multiple transmit
queues.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
