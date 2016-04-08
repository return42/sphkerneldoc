
.. _API-netif-tx-lock:

=============
netif_tx_lock
=============

*man netif_tx_lock(9)*

*4.6.0-rc1*

grab network device transmit lock


Synopsis
========

.. c:function:: void netif_tx_lock( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Get network device transmit lock
