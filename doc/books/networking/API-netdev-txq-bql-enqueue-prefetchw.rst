.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-txq-bql-enqueue-prefetchw:

================================
netdev_txq_bql_enqueue_prefetchw
================================

*man netdev_txq_bql_enqueue_prefetchw(9)*

*4.6.0-rc5*

prefetch bql data for write


Synopsis
========

.. c:function:: void netdev_txq_bql_enqueue_prefetchw( struct netdev_queue * dev_queue )

Arguments
=========

``dev_queue``
    pointer to transmit queue


Description
===========

BQL enabled drivers might use this helper in their ``ndo_start_xmit``,
to give appropriate hint to the CPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
