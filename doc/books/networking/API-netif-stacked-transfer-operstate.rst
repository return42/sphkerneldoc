
.. _API-netif-stacked-transfer-operstate:

================================
netif_stacked_transfer_operstate
================================

*man netif_stacked_transfer_operstate(9)*

*4.6.0-rc1*

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

Transfer operational state from root to device. This is normally called when a stacking relationship exists between the root device and the device(a leaf device).
