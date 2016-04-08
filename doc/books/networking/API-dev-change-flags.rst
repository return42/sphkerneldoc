
.. _API-dev-change-flags:

================
dev_change_flags
================

*man dev_change_flags(9)*

*4.6.0-rc1*

change device settings


Synopsis
========

.. c:function:: int dev_change_flags( struct net_device * dev, unsigned int flags )

Arguments
=========

``dev``
    device

``flags``
    device state flags


Description
===========

Change settings on device based state flags. The flags are in the userspace exported format.
