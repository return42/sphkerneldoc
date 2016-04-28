.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-change-flags:

================
dev_change_flags
================

*man dev_change_flags(9)*

*4.6.0-rc5*

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

Change settings on device based state flags. The flags are in the
userspace exported format.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
