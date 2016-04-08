
.. _API-netdev-txq-bql-complete-prefetchw:

=================================
netdev_txq_bql_complete_prefetchw
=================================

*man netdev_txq_bql_complete_prefetchw(9)*

*4.6.0-rc1*

prefetch bql data for write


Synopsis
========

.. c:function:: void netdev_txq_bql_complete_prefetchw( struct netdev_queue * dev_queue )

Arguments
=========

``dev_queue``
    pointer to transmit queue


Description
===========

BQL enabled drivers might use this helper in their TX completion path, to give appropriate hint to the CPU.
