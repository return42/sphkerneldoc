
.. _API---dev-get-by-index:

==================
__dev_get_by_index
==================

*man __dev_get_by_index(9)*

*4.6.0-rc1*

find a device by its ifindex


Synopsis
========

.. c:function:: struct net_device ⋆ __dev_get_by_index( struct net * net, int ifindex )

Arguments
=========

``net``
    the applicable net namespace

``ifindex``
    index of device


Description
===========

Search for an interface by index. Returns ``NULL`` if the device is not found or a pointer to the device. The device has not had its reference counter increased so the caller must
be careful about locking. The caller must hold either the RTNL semaphore or ``dev_base_lock``.
