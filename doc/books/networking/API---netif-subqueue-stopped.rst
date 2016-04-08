
.. _API---netif-subqueue-stopped:

========================
__netif_subqueue_stopped
========================

*man __netif_subqueue_stopped(9)*

*4.6.0-rc1*

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

Check individual transmit queue of a device with multiple transmit queues.
