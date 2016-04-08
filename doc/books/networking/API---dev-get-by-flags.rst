
.. _API---dev-get-by-flags:

==================
__dev_get_by_flags
==================

*man __dev_get_by_flags(9)*

*4.6.0-rc1*

find any device with given flags


Synopsis
========

.. c:function:: struct net_device ⋆ __dev_get_by_flags( struct net * net, unsigned short if_flags, unsigned short mask )

Arguments
=========

``net``
    the applicable net namespace

``if_flags``
    IFF_⋆ values

``mask``
    bitmask of bits in if_flags to check


Description
===========

Search for any interface with the given flags. Returns NULL if a device is not found or a pointer to the device. Must be called inside ``rtnl_lock``, and result refcount is
unchanged.
