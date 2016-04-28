.. -*- coding: utf-8; mode: rst -*-

.. _API---dev-get-by-index:

==================
__dev_get_by_index
==================

*man __dev_get_by_index(9)*

*4.6.0-rc5*

find a device by its ifindex


Synopsis
========

.. c:function:: struct net_device * __dev_get_by_index( struct net * net, int ifindex )

Arguments
=========

``net``
    the applicable net namespace

``ifindex``
    index of device


Description
===========

Search for an interface by index. Returns ``NULL`` if the device is not
found or a pointer to the device. The device has not had its reference
counter increased so the caller must be careful about locking. The
caller must hold either the RTNL semaphore or ``dev_base_lock``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
