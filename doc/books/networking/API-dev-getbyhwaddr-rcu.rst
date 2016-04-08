
.. _API-dev-getbyhwaddr-rcu:

===================
dev_getbyhwaddr_rcu
===================

*man dev_getbyhwaddr_rcu(9)*

*4.6.0-rc1*

find a device by its hardware address


Synopsis
========

.. c:function:: struct net_device ⋆ dev_getbyhwaddr_rcu( struct net * net, unsigned short type, const char * ha )

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

Search for an interface by MAC address. Returns NULL if the device is not found or a pointer to the device. The caller must hold RCU or RTNL. The returned device has not had its
ref count increased and the caller must therefore be careful about locking
