
.. _API---dev-uc-unsync:

===============
__dev_uc_unsync
===============

*man __dev_uc_unsync(9)*

*4.6.0-rc1*

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
