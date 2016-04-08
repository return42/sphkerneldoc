
.. _API-dev-get-by-index:

================
dev_get_by_index
================

*man dev_get_by_index(9)*

*4.6.0-rc1*

find a device by its ifindex


Synopsis
========

.. c:function:: struct net_device ⋆ dev_get_by_index( struct net * net, int ifindex )

Arguments
=========

``net``
    the applicable net namespace

``ifindex``
    index of device


Description
===========

Search for an interface by index. Returns NULL if the device is not found or a pointer to the device. The device returned has had a reference added and the pointer is safe until
the user calls dev_put to indicate they have finished with it.
