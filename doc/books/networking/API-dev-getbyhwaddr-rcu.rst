.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-getbyhwaddr-rcu:

===================
dev_getbyhwaddr_rcu
===================

*man dev_getbyhwaddr_rcu(9)*

*4.6.0-rc5*

find a device by its hardware address


Synopsis
========

.. c:function:: struct net_device * dev_getbyhwaddr_rcu( struct net * net, unsigned short type, const char * ha )

Arguments
=========

``net``
    the applicable net namespace

``type``
    media type of device

``ha``
    hardware address


Description
===========

Search for an interface by MAC address. Returns NULL if the device is
not found or a pointer to the device. The caller must hold RCU or RTNL.
The returned device has not had its ref count increased and the caller
must therefore be careful about locking


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
