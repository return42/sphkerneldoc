.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-uc-unsync:

===============
__dev_uc_unsync
===============

*man __dev_uc_unsync(9)*

*4.6.0-rc5*

Remove synchronized addresses from device


Synopsis
========

.. c:function:: void __dev_uc_unsync( struct net_device * dev, int (*unsync) struct net_device *, const unsigned char * )

Arguments
=========

``dev``
    device to sync

``unsync``
    function to call if address should be removed


Description
===========

Remove all addresses that were added to the device by ``dev_uc_sync``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
