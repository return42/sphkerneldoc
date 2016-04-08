
.. _API---dev-mc-sync:

=============
__dev_mc_sync
=============

*man __dev_mc_sync(9)*

*4.6.0-rc1*

Synchonize device's multicast list


Synopsis
========

.. c:function:: int __dev_mc_sync( struct net_device * dev, int (*sync) struct net_device *, const unsigned char *, int (*unsync) struct net_device *, const unsigned char * )

Arguments
=========

``dev``
    device to sync

``sync``
    function to call if address should be added

``unsync``
    function to call if address should be removed


Description
===========

Add newly added addresses to the interface, and release addresses that have been deleted.
