
.. _API-netif-stop-subqueue:

===================
netif_stop_subqueue
===================

*man netif_stop_subqueue(9)*

*4.6.0-rc1*

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

Stop individual transmit queue of a device with multiple transmit queues.
