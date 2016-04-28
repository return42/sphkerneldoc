.. -*- coding: utf-8; mode: rst -*-

.. _API-netif-stacked-transfer-operstate:

================================
netif_stacked_transfer_operstate
================================

*man netif_stacked_transfer_operstate(9)*

*4.6.0-rc5*

transfer operstate


Synopsis
========

.. c:function:: void netif_stacked_transfer_operstate( const struct net_device * rootdev, struct net_device * dev )

Arguments
=========

``rootdev``
    the root or lower level device to transfer state from

``dev``
    the device to transfer operstate to


Description
===========

Transfer operational state from root to device. This is normally called
when a stacking relationship exists between the root device and the
device(a leaf device).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
