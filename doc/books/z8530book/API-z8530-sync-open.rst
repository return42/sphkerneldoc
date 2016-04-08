
.. _API-z8530-sync-open:

===============
z8530_sync_open
===============

*man z8530_sync_open(9)*

*4.6.0-rc1*

Open a Z8530 channel for PIO


Synopsis
========

.. c:function:: int z8530_sync_open( struct net_device * dev, struct z8530_channel * c )

Arguments
=========

``dev``
    The network interface we are using

``c``
    The Z8530 channel to open in synchronous PIO mode


Description
===========

Switch a Z8530 into synchronous mode without DMA assist. We raise the RTS/DTR and commence network operation.
