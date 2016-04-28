.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-mc-unsync:

===============
__dev_mc_unsync
===============

*man __dev_mc_unsync(9)*

*4.6.0-rc5*

Remove synchronized addresses from device


Synopsis
========

.. c:function:: void __dev_mc_unsync( struct net_device * dev, int (*unsync) struct net_device *, const unsigned char * )

Arguments
=========

``dev``
    device to sync

``unsync``
    function to call if address should be removed


Description
===========

Remove all addresses that were added to the device by ``dev_mc_sync``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
