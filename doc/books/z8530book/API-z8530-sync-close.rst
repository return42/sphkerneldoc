
.. _API-z8530-sync-close:

================
z8530_sync_close
================

*man z8530_sync_close(9)*

*4.6.0-rc1*

Close a PIO Z8530 channel


Synopsis
========

.. c:function:: int z8530_sync_close( struct net_device * dev, struct z8530_channel * c )

Arguments
=========

``dev``
    Network device to close

``c``
    Z8530 channel to disassociate and move to idle


Description
===========

Close down a Z8530 interface and switch its interrupt handlers to discard future events.
