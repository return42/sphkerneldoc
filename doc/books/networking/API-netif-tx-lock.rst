.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-tx-lock:

=============
netif_tx_lock
=============

*man netif_tx_lock(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
