.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-mc-sync:

=============
__dev_mc_sync
=============

*man __dev_mc_sync(9)*

*4.6.0-rc5*

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

Add newly added addresses to the interface, and release addresses that
have been deleted.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
