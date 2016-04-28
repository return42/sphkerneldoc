.. -*- coding: utf-8; mode: rst -*-

.. _API-dev-get-by-index-rcu:

====================
dev_get_by_index_rcu
====================

*man dev_get_by_index_rcu(9)*

*4.6.0-rc5*

find a device by its ifindex


Synopsis
========

.. c:function:: struct net_device * dev_get_by_index_rcu( struct net * net, int ifindex )

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
caller must hold RCU lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
